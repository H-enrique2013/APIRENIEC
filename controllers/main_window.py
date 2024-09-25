import pandas as pd
import os
from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType


class ConsultaSpark:
    def __init__(self):

        self.df_inicial=None
        self.spark = SparkSession.builder \
            .appName("Lectura de archivo") \
            .config("spark.executor.memory", "8g") \
            .config("spark.driver.memory", "4g") \
            .config("spark.executor.cores", "4") \
            .config("spark.sql.shuffle.partitions", "50") \
            .getOrCreate()
        
        self.cached_data = None

    def realizar_consulta(self):
        # Si ya existe un DataFrame en cachÃ©, reutilizarlo
        if self.cached_data:
            print("Usando datos en cachÃ©")
            return self.cached_data
        
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

        try:
            self.df_inicial = self.spark.read \
                .option("delimiter", "|") \
                .schema(schema) \
                .csv("/data/reniec.txt") \
                .repartition("DNI")
            # Almacenar el DataFrame en cachÃ©
            self.cached_data = self.df_inicial.cache()
            # Retornar los datos
            return self.cached_data
        except Exception as e:
            print(f"Error al leer el archivo: {e}")


class ListBookWindow():

    def ConsultaxDNINombresApellidos(self,typeconsulta,dni, Nom, Ap_pat, Ap_mat):
        consultaSpark = ConsultaSpark()
        #DataFrame
        self.df=consultaSpark.realizar_consulta()
        if typeconsulta=='0':
            resultado = self.df.filter(self.df["DNI"] == dni)
        elif typeconsulta=='1':
            if Nom != "" and Ap_pat != "" and Ap_mat != "":
                resultado = self.df.filter((self.df["NOMBRES"] == Nom) & (self.df["AP_PAT"] == Ap_pat) & (self.df["AP_MAT"] == Ap_mat))
                
            elif Nom == "" and Ap_pat != "" and Ap_mat != "":
                resultado = self.df.filter((self.df["AP_PAT"] == Ap_pat) & (self.df["AP_MAT"] == Ap_mat))
            
        # Selecciona solo las columnas requeridas
        resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
        
        # Convierte el DataFrame a una lista de tuplas
        resultado_tuplas = [tuple(row) for row in resultado_seleccionado.collect()]

        return resultado_tuplas
    
    #Funcion carga masiva dde DNI
    
    def CargaMasivaDNI(self,lista_dni):
        consultaSpark = ConsultaSpark()
        #DataFrame
        self.df=consultaSpark.realizar_consulta()
        # Filtrar el DataFrame por los números de DNI especificados
        resultado = self.df.filter(self.df['DNI'].isin(lista_dni))
        # Selecciona solo las columnas requeridas
        resultado_seleccionado = resultado.select("DNI", "NOMBRES", "AP_PAT", "AP_MAT", "FECHA_NAC", "DIRECCION", "EST_CIVIL", "MADRE", "PADRE","SEXO")
        # Convierte el DataFrame a una lista de tuplas
        resultado_tuplas = [tuple(row) for row in resultado_seleccionado.collect()]
        
        return resultado_tuplas
    

    def CargaMasivaPlantillaDNI(self,lista_dni):
        consultaSpark = ConsultaSpark()
        #DataFrame
        self.df=consultaSpark.realizar_consulta()
        # Filtrar el DataFrame por los números de DNI especificados
        resultado = self.df.filter(self.df['DNI'].isin(lista_dni))
        # Selecciona solo las columnas requeridas
        resultado_seleccionado = resultado.select("DNI", "AP_PAT", "AP_MAT","NOMBRES","SEXO","FECHA_NAC", "DIRECCION","UBIGEO_DIR","UBIGEO_NAC","EST_CIVIL","PADRE", "MADRE")
        
        return resultado_seleccionado
    
    
    def seleccionar_archivo_xlsx(self,df):
        dfDNI = df
        lista_DNI = dfDNI['DNI'].tolist()
        resultado_tuplas = self.CargaMasivaDNI(lista_DNI)
        return resultado_tuplas
        
        
    def seleccionar_archivo_Plantilla_xlsx(self,dfPlantilla):
        
        dfDNI = dfPlantilla
        lista_DNI = dfDNI['DNI'].tolist()
        
        DataFrameSpark = self.CargaMasivaPlantillaDNI(lista_DNI)
        Pandas_DataFrameSpark = DataFrameSpark.toPandas()
        
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
        dfUbigeos=pd.read_excel("./geodir-ubigeo-reniec.xlsx",dtype={"Ubigeo":str})
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
        print("**********************************************************")
        print("DNI NO ENCONTRADOS :",lista_DNI_NoEncontrados)

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
        return DtaTuplas_Plantilla
       

