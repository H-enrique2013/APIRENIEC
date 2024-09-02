#!/bin/bash

# Iniciar Spark en segundo plano
$SPARK_HOME/sbin/start-master.sh &
$SPARK_HOME/sbin/start-worker.sh spark://localhost:7077 &

# Iniciar la aplicación Flask con Gunicorn
gunicorn -b 0.0.0.0:8000 main:app --timeout 120 --access-logfile /tmp/gunicorn_access.log --error-logfile /tmp/gunicorn_error.log
