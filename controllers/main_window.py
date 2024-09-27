import pandas as pd
import os


class ListBookWindow():
    
    def seleccionar_archivo_Plantilla_xlsx(self,dfArchivo,dfresultado):
        
        dfDNI = dfArchivo
        lista_DNI=dfDNI['DNI'].tolist()
        DataFrameSpark = dfresultado
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
       

