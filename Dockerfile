FROM python:3.10.11

# Instalar OpenJDK
RUN apt-get update && apt-get install -y openjdk-17-jdk

# Configurar JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Descargar e instalar Spark
RUN curl -sL https://archive.apache.org/dist/spark/spark-3.5.2/spark-3.5.2-bin-hadoop3.tgz | tar xz -C /opt
ENV SPARK_HOME=/opt/spark-3.5.2-bin-hadoop3
ENV PATH=$SPARK_HOME/bin:$PATH

# Copiar archivos de la aplicación
COPY . /app

# Instalar dependencias
WORKDIR /app
RUN pip install -r requirements.txt

# Exponer el puerto
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "main:app"]

