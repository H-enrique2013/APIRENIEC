from flask import Flask, request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
import pandas as pd
from controllers.main_window import ListBookWindow
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType
import atexit
import logging
import os
from pyspark import StorageLevel  # Importar StorageLevel

# Configurar logging
logging.basicConfig(level=logging.INFO)

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
            .persist(StorageLevel.DISK_ONLY)  # Cambiado a persistir en disco
        
        # Ejecutar una acción para cachear
        self.df.count()  # Acción que activa el cacheo
        self.list_book_window = ListBookWindow()

    def validar_archivo_excel(self, archivo_nombre):
        """Valida que el archivo subido sea un archivo de Excel válido"""
        archivo = request.files.get(archivo_nombre)

        if not archivo:
            return jsonify({"error": "No se ha subido ningún archivo"}), 400

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

        @app.route('/consultaDNINombresApellidos', methods=['POST'])
        def consultaDNINombresApellidos():
            try:
                data = request.get_json()
                Typeconsulta = data.get('Typeconsulta', '')
                n_dni = data.get('N_DNI', '')
                Nom = data.get('Nombres', '').upper()
                Ap_Pat = data.get('Ap_Paterno', '').upper()
                Ap_Mat = data.get('Ap_Materno', '').upper()

                if Typeconsulta not in ['0', '1']:
                    return jsonify({"error": f"Typeconsulta debe ser solo 0 o 1: {Typeconsulta}"}), 400
                
                if Typeconsulta == '0':
                    if not n_dni or len(n_dni) != 8 or not n_dni.isdigit():
                        return jsonify({"error": "DNI inválido. Debe ser un número de 8 dígitos"}), 400
                    resultado = self.df.filter(self.df["DNI"] == n_dni)
                elif Typeconsulta == '1':
                    if (not Nom and (not Ap_Pat or not Ap_Mat)) or (not Ap_Pat or not Ap_Mat):
                        return jsonify({"error": "Debe ingresar Ap_Paterno y Ap_Materno, y opcionalmente Nombres"}), 400

                    if Nom and Ap_Pat and Ap_Mat:
                        resultado = self.df.filter((self.df["NOMBRES"] == Nom) & (self.df["AP_PAT"] == Ap_Pat) & (self.df["AP_MAT"] == Ap_Mat))
                    else:
                        resultado = self.df.filter((self.df["AP_PAT"] == Ap_Pat) & (self.df["AP_MAT"] == Ap_Mat))

                resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE", "SEXO")
                ResultadoConsulta = [tuple(row) for row in resultado_seleccionado.collect()]

                if ResultadoConsulta:
                    return jsonify(ResultadoConsulta), 200
                else:
                    return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404
            except Exception as e:
                logging.error(f"Error en consultaDNINombresApellidos: {e}")
                return jsonify({"error": f"Ha ocurrido un error: {str(e)}"}), 500

        @app.route('/cargamasivaDNI', methods=['POST'])
        def cargamasivaDNI():
            archivo, error = self.validar_archivo_excel('archivo_excel')
            if error:
                return error
            
            try:
                df_archivo = pd.read_excel(archivo, dtype={'DNI': str})
                lista_dni = df_archivo['DNI'].tolist()
                resultado = self.df.filter(self.df['DNI'].isin(lista_dni))
                resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE", "SEXO")
                ResultadoConsulta = [tuple(row) for row in resultado_seleccionado.collect()]

                if ResultadoConsulta:
                    return jsonify(ResultadoConsulta), 200
                else:
                    return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404
            except Exception as e:
                logging.error(f"Error en cargamasivaDNI: {e}")
                return jsonify({"error": str(e)}), 500

        if __name__ == "__main__":
            # Obtener el puerto del entorno, si está disponible
            port = int(os.environ.get('PORT', 8000))
            logging.info(f"Iniciando servidor en el puerto {port}")
            app.run(host='0.0.0.0', port=port)


if __name__ == "__main__":
    api_reniec = Api_Reniec()

    @atexit.register
    def cerrar_spark():
        api_reniec.df.unpersist()
        api_reniec.spark.stop()
        logging.info("Spark detenido y caché liberado")

    try:
        api_reniec.run()
    except Exception as e:
        logging.error(f"Ocurrió un error al ejecutar la aplicación: {e}")



