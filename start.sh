#!/bin/bash

gunicorn -b 0.0.0.0:8000 main:app \
--timeout 120 \
--access-logfile - \
--error-logfile -