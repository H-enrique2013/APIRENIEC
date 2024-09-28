#!/bin/bash

# Iniciar la aplicación Flask con Gunicorn
gunicorn -b 0.0.0.0:8000 main:app --timeout 120 --access-logfile /tmp/gunicorn_access.log --error-logfile /tmp/gunicorn_error.log
#!/bin/bash

# Iniciar la aplicación Flask con Gunicorn y registrar la salida
#gunicorn -b 0.0.0.0:8000 main:app --timeout 120 --access-logfile /tmp/gunicorn_access.log --error-logfile /tmp/gunicorn_error.log
