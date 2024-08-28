# Usa una imagen base oficial de Python
FROM python:3.11-slim

# Instala Java (OpenJDK 17 en este caso) y ncurses-base para tput
RUN apt-get update && apt-get install -y --no-install-recommends \
    openjdk-17-jdk \
    wget \
    ncurses-base \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establece la variable JAVA_HOME y añade Java al PATH
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV PATH="$JAVA_HOME/bin:$PATH"

# Verifica la instalación de Java
RUN java -version

# Descargar e instalar Spark
RUN wget https://archive.apache.org/dist/spark/spark-3.5.2/spark-3.5.2-bin-hadoop3.tgz -O spark.tgz \
    && tar -xzf spark.tgz -C /opt \
    && rm spark.tgz \
    && mv /opt/spark-3.5.2-bin-hadoop3 /opt/spark \
    && ln -s /opt/spark/bin/spark-submit /usr/local/bin/spark-submit

# Verificar la instalación de Spark
RUN ls -l /opt/spark/bin && \
    /opt/spark/bin/spark-submit --version

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
