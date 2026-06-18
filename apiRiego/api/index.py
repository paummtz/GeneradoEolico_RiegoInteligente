import sys
import os

# Como moviste api/ a la raíz, solo necesitas subir un nivel
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from Directions import app