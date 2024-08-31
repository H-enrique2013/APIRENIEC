# Usar una imagen base de Python
FROM python:3.10.11-slim

# Instalar dependencias necesarias para Java, Spark y Hadoop
RUN apt-get update && apt-get install -y \
    curl \
    openjdk-17-jdk \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

# Establecer las variables de entorno de Java, Spark y Hadoop
ENV JAVA_HOME=/usr/lib/jvm/java-17-openjdk-amd64
ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3.3.6
ENV SPARK_HOME=/opt/spark
ENV HADOOP_HOME=/opt/hadoop
ENV PATH=$PATH:$JAVA_HOME/bin:$SPARK_HOME/bin:$HADOOP_HOME/bin

# Descargar y descomprimir Apache Spark con Hadoop
RUN curl -fSL https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop3.tgz -o spark.tgz && \
    tar -xzf spark.tgz -C /opt/ && \
    mv /opt/spark-$SPARK_VERSION-bin-hadoop3 $SPARK_HOME && \
    rm spark.tgz

# Descargar y descomprimir Hadoop
RUN curl -fSL https://downloads.apache.org/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz -o hadoop.tar.gz && \
    tar -xzf hadoop.tar.gz -C /opt/ && \
    mv /opt/hadoop-$HADOOP_VERSION /opt/hadoop && \
    rm hadoop.tar.gz

# Ajustar permisos de ejecución para Spark y Hadoop
RUN chmod +x $SPARK_HOME/bin/* && chmod +x $HADOOP_HOME/bin/*

# Verificar que Spark y Hadoop están correctamente configurados
RUN ls -l $SPARK_HOME/bin/ && ls -l $HADOOP_HOME/bin/
RUN echo $JAVA_HOME && echo $SPARK_HOME && echo $HADOOP_HOME && echo $PATH

# Establecer el PATH para incluir el directorio de instalación de gunicorn
ENV PATH="/home/appuser/.local/bin:${PATH}"

# Ejecutar como root hasta que todas las instalaciones estén completas
RUN pip install --upgrade pip

# Crear el usuario y cambiar permisos en el directorio de trabajo
RUN useradd -ms /bin/sh appuser

# Cambiar al directorio de trabajo antes de copiar los archivos
WORKDIR /app

# Copiar los archivos de la aplicación
COPY . .

# Copiar el archivo de requisitos
COPY requirements.txt .

# Instalar dependencias usando pip como root
RUN pip install --no-cache-dir -r requirements.txt

# Cambiar los permisos de la carpeta de trabajo a appuser
RUN chown -R appuser:appuser /app

# Cambiar al usuario no root
USER appuser

# Exponer el puerto para la aplicación Flask
EXPOSE 8000

# Comando para ejecutar gunicorn
CMD ["gunicorn", "-b", "0.0.0.0:8000", "main:app"]
