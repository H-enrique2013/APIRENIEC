# Usa una imagen base oficial de Python
FROM python:3.10.11

# Instala Java (OpenJDK 17 en este caso)
RUN apt-get update && apt-get install -y openjdk-17-jdk

# Establece la variable JAVA_HOME
ENV JAVA_HOME /usr/lib/jvm/java-17-openjdk-amd64

# Asegúrate de que java está en el PATH
ENV PATH="$JAVA_HOME/bin:$PATH"

# Verifica la instalación de Java
RUN java -version

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
