# Usa una imagen base oficial de Python
FROM python:3.10.11

# Instala Java (OpenJDK 17 en este caso)
RUN apt-get update && apt-get install -y openjdk-17-jdk && apt-get clean

# Establece la variable JAVA_HOME y añade Java al PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Verifica la instalación de Java
RUN java -version

# Instala Spark
RUN apt-get update && apt-get install -y curl && \
    curl -O https://dlcdn.apache.org/spark/spark-3.5.2/spark-3.5.2-bin-hadoop3.tgz && \
    tar -xvf spark-3.5.2-bin-hadoop3.tgz && \
    mv spark-3.5.2-bin-hadoop3 /opt/spark && \
    rm spark-3.5.2-bin-hadoop3.tgz

# Configura SPARK_HOME y añade Spark al PATH
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

# Copia el archivo requirements.txt e instala las dependencias de Python
COPY requirements.txt /app/
WORKDIR /app
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código fuente
COPY . /app/

# Expone el puerto 8000
EXPOSE 8000

# Comando por defecto para iniciar la aplicación
CMD ["gunicorn", "-b", ":8000", "main:app"]

