# Usa una imagen base oficial de Python
FROM python:3.10.11

# Instala Java (OpenJDK 17 en este caso)
RUN apt-get update && apt-get install -y openjdk-17-jdk

# Establece la variable JAVA_HOME
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64

# Asegúrate de que java está en el PATH
ENV PATH="$JAVA_HOME/bin:$PATH"

# Verifica la instalación de Java
RUN java -versioncls

# Copia el archivo requirements.txt y el código fuente
COPY requirements.txt /app/
COPY . /app/

# Establece el directorio de trabajo
WORKDIR /app

# Instala las dependencias de Python
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que tu aplicación corre
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["gunicorn", "-b", ":8000", "main:app"]
RUN echo $JAVA_HOME
RUN apt-get update && \
    apt-get install -y openjdk-17-jdk && \
    apt-get clean;

ENV JAVA_HOME="/usr/lib/jvm/java-17-openjdk-amd64"
ENV PATH="${JAVA_HOME}/bin:${PATH}"
# Instalar Spark
RUN apt-get update && apt-get install -y curl && \
    curl -O https://dlcdn.apache.org/spark/spark-3.5.2/spark-3.5.2-bin-hadoop3.tgz && \
    tar -xvf spark-3.5.2-bin-hadoop3.tgz && \
    mv spark-3.5.2-bin-hadoop3 /opt/spark && \
    rm spark-3.5.2-bin-hadoop3.tgz

# Configurar SPARK_HOME
ENV SPARK_HOME="/opt/spark"
ENV PATH="$SPARK_HOME/bin:$PATH"
RUN echo $SPARK_HOME
