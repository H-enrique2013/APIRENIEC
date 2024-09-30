from flask import Flask, request, jsonify, send_from_directory, render_template
from werkzeug.utils import secure_filename
import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StringType
import atexit
import logging
import os
from pyspark import StorageLevel  # Importar StorageLevel
from pyspark.sql import functions as F

# Configurar logging
logging.basicConfig(level=logging.INFO)

app = Flask(__name__, template_folder='templates')

class Api_Reniec():
    
    def __init__(self):
        self.spark = SparkSession.builder \
            .appName("Lectura de archivo") \
            .config("spark.executor.memory", "8g") \
            .config("spark.driver.memory", "2g") \
            .config("spark.executor.cores", "2") \
            .config("spark.sql.shuffle.partitions", "5") \
            .getOrCreate()
        
        # Registrar la función de cierre de Spark
        atexit.register(self.cerrar_spark)
        self.schema = StructType() \
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
    
    def cerrar_spark(self):
        if self.spark is not None:
            try:
                self.spark.stop()
                logging.info("Sesión de Spark cerrada correctamente.")
            except Exception as e:
                logging.error(f"Error al cerrar la sesión de Spark: {e}")
        else:
            logging.warning("No hay una sesión de Spark activa para cerrar.")

    
    def cargar_parte_relevante(self, filtro):
        """Carga solo la parte relevante del archivo según el filtro"""
        df = self.spark.read \
            .option("delimiter", "|") \
            .schema(self.schema) \
            .csv("/data/reniec.txt") \
            .repartition(5) \
            .filter(filtro)
        return df

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
                    filtro = f"DNI = '{n_dni}'"
                elif Typeconsulta == '1':
                    if (not Nom and (not Ap_Pat or not Ap_Mat)) or (not Ap_Pat or not Ap_Mat):
                        return jsonify({"error": "Debe ingresar Ap_Paterno y Ap_Materno, y opcionalmente Nombres"}), 400

                    if Nom and Ap_Pat and Ap_Mat:
                        filtro = f"NOMBRES = '{Nom}' AND AP_PAT = '{Ap_Pat}' AND AP_MAT = '{Ap_Mat}'"
                    else:
                        filtro = f"AP_PAT = '{Ap_Pat}' AND AP_MAT = '{Ap_Mat}'"

                resultado = self.cargar_parte_relevante(filtro)
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
                lista_DNI = df_archivo['DNI'].tolist()
                filtro = F.col("DNI").isin(lista_DNI)
                resultado = self.cargar_parte_relevante(filtro)
                resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE", "SEXO")
                ResultadoConsulta = [tuple(row) for row in resultado_seleccionado.collect()]

                if ResultadoConsulta:
                    return jsonify(ResultadoConsulta), 200
                else:
                    return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404
            except Exception as e:
                logging.error(f"Error en cargamasivaDNI: {e}")
                return jsonify({"error": str(e)}), 500
            
        @app.route('/cargamasivaplantillaDNI', methods=['POST'])
        def cargamasivaplantillaDNI():
            archivo, error = self.validar_archivo_excel('archivoplantilla_excel')
            if error:
                return error
            try:
                # Leer el archivo Excel directamente en un DataFrame
                dfDNI = pd.read_excel(archivo,dtype={'DNI': str})
                dfUbigeos=pd.read_excel("geodir-ubigeo-reniec.xlsx",dtype={"Ubigeo":str})
                lista_DNI=dfDNI['DNI'].tolist()
                # Crea un filtro utilizando la función 'isin' de PySpark
                filtro = F.col("DNI").isin(lista_DNI)
                # Aplica el filtro directamente al DataFrame Spark
                resultado = self.cargar_parte_relevante(filtro)
                # Selecciona solo las columnas requeridas
                #DataFrameSpark = resultado.select("DNI", "AP_PAT", "AP_MAT","NOMBRES","SEXO","FECHA_NAC", "DIRECCION","UBIGEO_DIR","UBIGEO_NAC","EST_CIVIL","PADRE", "MADRE")
                # Supongamos que la función `seleccionar_archivo_xlsx` hace algún tipo de procesamiento
                #plantilla= self.list_book_window.seleccionar_archivo_Plantilla_xlsx(df_archivo,resultado_selec)
                Pandas_DataFrameSpark = resultado.toPandas()
                
                lista_DNI_Spark = Pandas_DataFrameSpark["DNI"].tolist()
                #Crear el Dataframe completo a la lista de DNI's  encontrados
                Nuevo_dfDNI = dfDNI[dfDNI["DNI"].isin(lista_DNI_Spark)].copy()  # Asegurarse de crear una copia

                # Evitar SettingWithCopyWarning usando .loc
                Nuevo_dfDNI.loc[:, 'DNI'] = Nuevo_dfDNI['DNI'].astype(str)
                Pandas_DataFrameSpark.loc[:, 'DNI'] = Pandas_DataFrameSpark['DNI'].astype(str)

                # Unir los DataFrames por la columna 'DNI', manteniendo el orden de Nuevo_dfDNI
                merged_df = pd.merge(Nuevo_dfDNI, Pandas_DataFrameSpark, on='DNI', how='left')
                
                # Seleccionar todas las columnas del segundo DataFrame excepto 'DNI' después de la fusión si es necesario
                merged_df = merged_df.drop(columns=['DNI_y']) if 'DNI_y' in merged_df.columns else merged_df
                
                # Separar los valores de la columna "UBIGEO_DIR" en nuevas columnas
                merged_df[['DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D']] = merged_df['UBIGEO_DIR'].str.split('-', expand=True)
                merged_df["UBIGEO_DIR"]=" "
                #Cargar Ubigeos
                dfUbigeos=dfUbigeos.drop(["Poblacion","Superficie","Y","X"],axis=1)
                dfUbigeos_nac = dfUbigeos.rename(columns={
                    "Ubigeo": "UBIGEO_NAC",
                    "Distrito": "DISTRITO_N",
                    "Provincia": "PROVINCIA_N",
                    "Departamento": "DEPARTAMENTO_N"
                })
                
                merged_df1 = pd.merge(merged_df,dfUbigeos_nac, on='UBIGEO_NAC', how='left')
                merged_df2 = merged_df1[["DNI","Superficie","Monto_Indemnizable","AP_PAT_ENTRADA","AP_MAT_ENTRADA","NOMBRES_ENTRADA","FECHA_NAC_ENTRADA",
                                        "AP_PAT", "AP_MAT","NOMBRES","SEXO","FECHA_NAC","EST_CIVIL","DIRECCION","UBIGEO_DIR","DEPARTAMENTO_D","PROVINCIA_D","DISTRITO_D",
                                        "PADRE","MADRE","UBIGEO_NAC","DEPARTAMENTO_N","PROVINCIA_N","DISTRITO_N"]]
                
                #Realizar el codigo para completar la columna "UBIGEO_DIR" que está vacia
                #Renombrar las columnas de dfUbigeos_nac
                dfUbigeos_nac_renamed = dfUbigeos_nac.rename(columns={
                        "DEPARTAMENTO_N": "DEPARTAMENTO_DIR",
                        "PROVINCIA_N": "PROVINCIA_DIR",
                        "DISTRITO_N": "DISTRITO_DIR",
                        "UBIGEO_NAC": "UBIGEO_DIR_TEMP"
                    })
                
                #Realizar el merge condicional
                merged_df2 = merged_df2.merge(dfUbigeos_nac_renamed[['DEPARTAMENTO_DIR', 'PROVINCIA_DIR', 'DISTRITO_DIR', 'UBIGEO_DIR_TEMP']],
                                    left_on=['DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D'],
                                    right_on=['DEPARTAMENTO_DIR', 'PROVINCIA_DIR', 'DISTRITO_DIR'],
                                    how='left')
                
                #Completar la columna UBIGEO_DIR
                merged_df2['UBIGEO_DIR'] = merged_df2['UBIGEO_DIR_TEMP']
                #Limpiar el DataFrame
                merged_df2.drop(columns=['DEPARTAMENTO_DIR', 'PROVINCIA_DIR', 'DISTRITO_DIR', 'UBIGEO_DIR_TEMP'], inplace=True)

                #########################################################################################
                lista_DNI_NoEncontrados=[]
                #Crear el Dataframe completo a la lista de DNI's no encontrados
                for i in lista_DNI:
                    if not i in lista_DNI_Spark:
                        lista_DNI_NoEncontrados.append(i)
                
                if len(lista_DNI_NoEncontrados)!=0:
                    Nuevo_dfDNI_NoEncontrados=dfDNI[dfDNI["DNI"].isin(lista_DNI_NoEncontrados)].copy()
                    # Lista de nombres de las nuevas columnas
                    columnas_nuevas = ['AP_PAT', 'AP_MAT', 'NOMBRES', 'SEXO', 'FECHA_NAC', 'DIRECCION','UBIGEO_DIR',
                                    'DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D', 'PADRE','MADRE', 'UBIGEO_NAC',
                                    'DEPARTAMENTO_N', 'PROVINCIA_N', 'DISTRITO_N']

                    # Añadir las columnas nuevas con campos vacios " "
                    for columna in columnas_nuevas:
                        Nuevo_dfDNI_NoEncontrados[columna] =' '
                    
                    merged_df2=pd.concat([merged_df2, Nuevo_dfDNI_NoEncontrados], ignore_index=True)

                DtaTuplas_Plantilla = merged_df2.values.tolist()
                
                # Verificar si el resultado es válido
                if DtaTuplas_Plantilla:
                    return jsonify(DtaTuplas_Plantilla), 200
                else:
                    return jsonify({"error": "No se encontró información para los datos proporcionados"}), 404
            except Exception as e:
                return jsonify({"error": str(e)}), 500
        return app

# Instanciar Api_Reniec fuera del bloque principal
api_reniec = Api_Reniec()

# Exponer el objeto Flask para Gunicorn
app = api_reniec.run()

if __name__ == "__main__":
    # Obtener el puerto del entorno, si está disponible
    port = int(os.environ.get('PORT', 8000))
    logging.info(f"Iniciando servidor en el puerto {port}")
    app.run(host='0.0.0.0', port=port)

