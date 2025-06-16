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
        #merged_df[['DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D']] = merged_df['UBIGEO_DIR'].str.split('-', expand=True)
        # Asegura que no haya nulos
        # Procesar UBIGEO_DIR
        merged_df['UBIGEO_DIR'] = merged_df['UBIGEO_DIR'].fillna("")

        # Hacer el split en máximo 3 columnas (si hay más, se ignoran; si hay menos, se rellenan)
        split_cols = merged_df['UBIGEO_DIR'].str.split('-', expand=True)

        # Forzar que tenga exactamente 3 columnas
        for i in range(3):
            if i not in split_cols.columns:
                split_cols[i] = ""

        # Tomar solo las 3 primeras columnas
        split_cols = split_cols[[0, 1, 2]].fillna("")

        # Asignar con nombres
        merged_df[['DEPARTAMENTO_D', 'PROVINCIA_D', 'DISTRITO_D']] = split_cols

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
        merged_df2 = merged_df1[["DNI","Superficie","Monto_Indemnizable","TIPO_DE_ASCENDENCIA","TELEFONO","AP_PAT_ENTRADA","AP_MAT_ENTRADA","NOMBRES_ENTRADA","FECHA_NAC_ENTRADA",
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
        
        if len(lista_DNI_NoEncontrados) != 0:
            # Filtrar los DNIs no encontrados
            Nuevo_dfDNI_NoEncontrados = dfDNI[dfDNI["DNI"].isin(lista_DNI_NoEncontrados)].copy()

            # Crear columnas faltantes con valores vacíos
            columnas_faltantes = list(set(merged_df2.columns) - set(Nuevo_dfDNI_NoEncontrados.columns))
            for columna in columnas_faltantes:
                Nuevo_dfDNI_NoEncontrados[columna] = ' '

            # Asegurar que el orden de columnas sea el mismo que en merged_df2
            Nuevo_dfDNI_NoEncontrados = Nuevo_dfDNI_NoEncontrados[merged_df2.columns]

            # Concatenar los DataFrames
            merged_df2 = pd.concat([merged_df2, Nuevo_dfDNI_NoEncontrados], ignore_index=True)
        DtaTuplas_Plantilla = merged_df2.values.tolist()
        return DtaTuplas_Plantilla
