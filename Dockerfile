# Usar una imagen base de Python
FROM python:3.10.11-slim

# Instalar dependencias necesarias para Java, Spark y Hadoop
RUN apt-get update && apt-get install -y \
    curl \
    openjdk-17-jdk \
    && apt-get clean

# Establecer las variables de entorno de Java, Spark y Hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3.3.6
ENV SPARK_HOME=/opt/spark
ENV HADOOP_HOME=/opt/hadoop
ENV PATH="$SPARK_HOME/bin:$HADOOP_HOME/bin:$PATH"

# Descargar y descomprimir Apache Spark con Hadoop
RUN curl -fSL https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz -o spark.tgz && \
    tar -xzf spark.tgz -C /opt/ && \
    mv /opt/spark-$SPARK_VERSION-bin-hadoop3 $SPARK_HOME && \
    rm spark.tgz

# Descargar y descomprimir Hadoop
RUN curl -fSL https://downloads.apache.org/hadoop/common/hadoop-3.3.6/hadoop-3.3.6.tar.gz -o hadoop.tar.gz && \
    tar -xzf hadoop.tar.gz -C /opt/ && \
    mv /opt/hadoop-3.3.6 /opt/hadoop && \
    rm hadoop.tar.gz


# Verificar que Spark y Hadoop están correctamente configurados
RUN ls -l $SPARK_HOME/bin/ && ls -l $HADOOP_HOME/bin/
RUN chmod +x $SPARK_HOME/bin/spark-submit
RUN echo $JAVA_HOME && echo $SPARK_HOME && echo $HADOOP_HOME && echo $PATH

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY . /app
COPY script.py /app/

# Instalar las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Exponer el puerto donde correrá tu aplicación
EXPOSE 8000

# Iniciar la aplicación con Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]
