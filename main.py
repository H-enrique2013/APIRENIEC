from flask import Flask, request, jsonify, send_from_directory, render_template, redirect, g
from werkzeug.utils import secure_filename
import pandas as pd
from controllers.main_window import ListBookWindow
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType
import atexit
import logging

app = Flask(__name__, template_folder='templates')



class Api_Reniec():
    
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("Lectura de archivo") \
            .config("spark.executor.memory", "2g") \
            .config("spark.driver.memory", "1g") \
            .config("spark.executor.cores", "1") \
            .config("spark.sql.shuffle.partitions", "2") \
            .getOrCreate()

        schema = StructType() \
            .add("DNI", StringType(), True) \
            .add("AP_PAT", StringType(), True) \
            .add("AP_MAT", StringType(), True) \
            .add("NOMBRES", StringType(), True) \
            .add("FECHA_NAC", StringType(), True) \
            .add("UBIGEO_NAC", StringType(), True) \
            .add("UBIGEO_DIR", StringType(), True) \
            .add("DIRECCION", StringType(), True) \
            .add("SEXO", StringType(), True) \
            .add("EST_CIVIL", StringType(), True) \
            .add("MADRE", StringType(), True) \
            .add("PADRE", StringType(), True)

        self.df = self.spark.read \
            .option("delimiter", "|") \
            .schema(schema) \
            .csv("/data/reniec.txt") \
            .repartition(2) \
            .cache()  # Cachear el DataFrame
        
        # Ejecutar una acción para cachear
        self.df.count()  # Acción que activa el cacheo
        self.list_book_window=ListBookWindow()
        
    def validar_archivo_excel(self, archivo, archivo_nombre):
        """Valida que el archivo subido sea un archivo de Excel válido"""
        if archivo_nombre not in request.files:
            return jsonify({"error": "No se ha subido ningún archivo"}), 400

        archivo = request.files[archivo_nombre]

        if archivo.filename == '':
            return jsonify({"error": "El archivo no tiene nombre"}), 400

        if not (archivo.filename.endswith('.xlsx') or archivo.filename.endswith('.xls')):
            return jsonify({"error": "Formato de archivo no soportado"}), 400
        
        return archivo, None

    def run(self):
        @app.route('/')
        def index():
            return render_template('index.html')

        @app.route('/Sispad.ico')
        def favicon():
            return send_from_directory('static', 'Sispad.ico', as_attachment=False)

        #Métodos POST
        @app.route('/consultaDNINombresApellidos', methods=['POST'])
        def consultaDNINombresApellidos():
            try:
                data = request.get_json()
                Typeconsulta = data.get('Typeconsulta', '')#Si es 0 busca por DNI y si es 1 busca por nomb y apellidos
                n_dni = data.get('N_DNI', '')
                Nom = data.get('Nombres', '').upper()  # Convertir a mayúsculas
                Ap_Pat = data.get('Ap_Paterno', '').upper()  # Convertir a mayúsculas
                Ap_Mat = data.get('Ap_Materno', '').upper()  # Convertir a mayúsculas

                if Typeconsulta!='0' and Typeconsulta!='1':
                    return jsonify({"error":f"Typeconsulta debe ser solo 0 o 1: {Typeconsulta}"})
                
                if Typeconsulta=='0':
                    # Validación del DNI
                    if not n_dni or len(n_dni) != 8 or not n_dni.isdigit():
                            return jsonify({"error": "DNI inválido. Debe ser un número de 8 dígitos"}), 400
                    resultado = self.df.filter(self.df["DNI"] == n_dni)
                elif Typeconsulta=='1':
                    # Validación de campos:
                    # Caso 1: Todos los campos deben ser diferentes de vacío
                    # Caso 2: Nom puede estar vacío, pero Ap_Pat y Ap_Mat deben ser diferentes de vacío
                    if (not Nom and (not Ap_Pat or not Ap_Mat)) or (not Ap_Pat or not Ap_Mat):
                        return jsonify({"error": "Debe ingresar Ap_Paterno y Ap_Materno, y opcionalmente Nombres"}), 400
                    if Nom != "" and Ap_Pat != "" and Ap_Mat != "":
                        resultado = self.df.filter((self.df["NOMBRES"] == Nom) & (self.df["AP_PAT"] == Ap_Pat) & (self.df["AP_MAT"] == Ap_Mat))
                    elif Nom == "" and Ap_Pat != "" and Ap_Mat != "":
                        resultado = self.df.filter((self.df["AP_PAT"] == Ap_Pat) & (self.df["AP_MAT"] == Ap_Mat))
                # Selecciona solo las columnas requeridas
                resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
                
                # Convierte el DataFrame a una lista de tuplas
                ResultadoConsulta = [tuple(row) for row in resultado_seleccionado.collect()]  
                # Verificar si el resultado es válido
                if ResultadoConsulta:
                    return jsonify(ResultadoConsulta), 200
                else:
                    return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404
            except Exception as e:
                return jsonify({"error": f"Ha ocurrido un error: {str(e)}"}), 500

        @app.route('/cargamasivaDNI', methods=['POST'])
        def cargamasivaDNI():
            archivo, error = self.validar_archivo_excel(request.files, 'archivo_excel')
            if error:
                return error
            
            try:
                # Leer el archivo Excel directamente en un DataFrame
                df_archivo = pd.read_excel(archivo,dtype={'DNI': str})

                lista_dni=df_archivo['DNI'].tolist()
                # Filtrar el DataFrame por los números de DNI especificados
                resultado = self.df.filter(self.df['DNI'].isin(lista_dni))
                # Selecciona solo las columnas requeridas
                resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
                # Convierte el DataFrame a una lista de tuplas
                ResultadoConsulta = [tuple(row) for row in resultado_seleccionado.collect()]
                # Verificar si el resultado es válido
                if ResultadoConsulta:
                    return jsonify(ResultadoConsulta), 200
                else:
                    return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404

            except Exception as e:
                return jsonify({"error": str(e)}), 500


        @app.route('/cargamasivaplatillaDNI', methods=['POST'])
        def cargamasivaplantillaDNI():
            archivo, error = self.validar_archivo_excel(request.files, 'archivoplantilla_excel')
            if error:
                return error

            try:
                # Leer el archivo Excel directamente en un DataFrame
                df_archivo = pd.read_excel(archivo,dtype={'DNI': str})
                lista_dni=df_archivo['DNI'].tolist()
                # Filtrar el DataFrame por los números de DNI especificados
                resultado = self.df.filter(self.df['DNI'].isin(lista_dni))
                # Selecciona solo las columnas requeridas
                resultado_selec = resultado.select("DNI", "AP_PAT", "AP_MAT","NOMBRES","SEXO","FECHA_NAC", "DIRECCION","UBIGEO_DIR","UBIGEO_NAC","EST_CIVIL","PADRE", "MADRE")
                
                # Supongamos que la función `seleccionar_archivo_xlsx` hace algún tipo de procesamiento
                plantilla= self.list_book_window.seleccionar_archivo_Plantilla_xlsx(df_archivo,resultado_selec)
                # Realiza operaciones con list_book_window...
                #list_book_window.stop_spark()
                
                # Verificar si el resultado es válido
                if plantilla:
                    return jsonify(plantilla), 200
                else:
                    return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404

            except Exception as e:
                return jsonify({"error": str(e)}), 500
            
        if __name__ == "__main__":
            try:
                app.run(host='0.0.0.0', port=8000)
            except Exception as e:
                print(f"Error occurred: {e}")




if __name__ == "__main__":
    api_reniec = Api_Reniec()

    @atexit.register
    def cerrar_spark():
        api_reniec.df.unpersist()  # Liberar el caché
        api_reniec.spark.stop()

    try:
        api_reniec.run()
    except Exception as e:
        logging.error(f"Ocurrió un error: {e}")