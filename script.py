import os
import subprocess

java_home = os.getenv('JAVA_HOME')
print(f"JAVA_HOME: {java_home}")

# Verificar la versión de Java
subprocess.run(["java", "-version"])

# Verificar la versión de Spark
subprocess.run([os.getenv('SPARK_HOME') + "/bin/spark-submit", "--version"])
