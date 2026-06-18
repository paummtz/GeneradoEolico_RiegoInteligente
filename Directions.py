import sys
import os

# Esto es vital: le dice a Python que busque módulos en la carpeta raíz
sys.path.append(os.getcwd())

# Importamos la variable 'app' desde el archivo Directions.py
from Directions import app

# Vercel usará automáticamente esta variable 'app' al importar este archivo
