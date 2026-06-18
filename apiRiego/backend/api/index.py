import sys
import os

# Configuración de ruta
ruta_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
if ruta_raiz not in sys.path:
    sys.path.append(ruta_raiz)

from Directions import app

# PRUEBA RÁPIDA: Imprimir las rutas configuradas
if __name__ == "__main__":
    print("¡La app se cargó correctamente!")
    print("Rutas detectadas:")
    for rule in app.url_map.iter_rules():
        print(f"{rule.endpoint}: {rule.rule}")
