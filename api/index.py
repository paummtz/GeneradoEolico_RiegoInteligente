import sys
import os

# Aseguramos que la carpeta raíz esté en el path de búsqueda
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importamos 'app' desde tu archivo principal Directions.py
from Directions import app

# Vercel necesita que 'app' sea la variable global exportada