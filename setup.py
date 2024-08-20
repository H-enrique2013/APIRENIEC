import sys
import os
from cx_Freeze import setup, Executable

files = ['assets', 'book_files', 'books_db.db', 'REPORTES', 'pys2_msgboxes']

exe = Executable(
    "app.py",  # Cambiado aquí
    base='Win32GUI',
    icon="logo_feban.ico",
)

setup(
    name="Sistema de Seguimiento al Contrato de Alarmas - Banco de la Nación",
    version="1.0",
    description="Sistema para ...",
    author="Hoz",
    options={'build_exe': {'include_files': files}},
    executables=[exe]
)
