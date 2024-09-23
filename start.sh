#!/bin/bash

# Iniciar la aplicación Flask con Gunicorn
gunicorn -b 0.0.0.0:8000 main:app --timeout 180 --access-logfile /tmp/gunicorn_access.log --error-logfile /tmp/gunicorn_error.log
