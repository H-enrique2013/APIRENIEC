# Usar una imagen base de Python
FROM python:3.10.11-slim

# Instalar dependencias necesarias para Java y Spark
RUN apt-get update && apt-get install -y \
    curl \
    openjdk-17-jdk \
    && apt-get clean

# Establecer las variables de entorno de Java y Spark
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV SPARK_VERSION=3.5.2
ENV SPARK_HOME=/opt/spark
ENV PATH="$SPARK_HOME/bin:$PATH"

# Descargar y descomprimir Apache Spark
RUN curl -O https://dlcdn.apache.org/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz && \
    tar -xzf spark-$SPARK_VERSION-bin-hadoop3.tgz -C /opt/ && \
    mv /opt/spark-$SPARK_VERSION-bin-hadoop3 $SPARK_HOME && \
    rm spark-$SPARK_VERSION-bin-hadoop3.tgz


RUN ls -l $SPARK_HOME/bin/
RUN chmod +x $SPARK_HOME/bin/spark-submit
RUN echo $JAVA_HOME && echo $SPARK_HOME && echo $PATH

# Configura el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto donde correrá tu aplicación
EXPOSE 8000

# Iniciar la aplicación con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
