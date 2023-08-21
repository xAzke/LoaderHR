import os, time

def checkearLib(libName):
    try:
        __import__(libName)
        return True
    except ImportError:
        return False

def instalarLib(libList):
    for libName in libList:
        if not checkearLib(libName):
            try:
                os.system(f"pip install {libName}")
                print(f"Libreria {libName} instalada correctamente.")
            except Exception as Error:
                print(f"Error al instalar la libreria {libName}: {Error}")
        else:
            print(f"La libreria {libName} ya esta instalada.")

def iniciarEjecucion():
    tiempoInicio = time.time()

    libList = [
        "pynput",
        "pyperclip",
    ]

    instalarLib(libList)

    try:
        import Funciones
        Funciones.iniciarConsola()
    except ImportError:
        print("Ocurrio un error al tratar de importar la libreria de funciones.")

    tiempoFinal = time.time()
    tiempoTotal = tiempoFinal - tiempoInicio
    print(f"Tiempo total de ejecución del script: {tiempoTotal:.2f} segundos")
    time.sleep(5)

if __name__ == "__main__":
    iniciarEjecucion()