import sys
import os

# Agregamos el directorio padre al path para que pueda encontrar 'Directions'
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Directions import app
