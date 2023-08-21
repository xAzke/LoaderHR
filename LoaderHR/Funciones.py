import os, shutil, pyperclip, pynput, time

from pynput.mouse import Button, Controller as MouseController
from pynput.keyboard import Key, Controller as KeyboardController

# Constantes.
TIME_WAIT_SHORT = 0.1
TIME_WAIT_LONG = 1

# Lista de comandos a ejecutar.
listaComandos = [
    "/as sysdba",
    'alter session set "_oracle_script"=true;',
    "DROP USER HR CASCADE;",
    "@?/demo/schema/human_resources/hr_main.sql",
    "P4$$woRD",
    "users",
    "temp",
    "$ORACLE_HOME/demo/schema/log/",
    "exit",
]

# Buscar la ruta de instalacion de SQLPlus.
SQLPlus_Path = shutil.which("SQLPlus")
if SQLPlus_Path is None:
    print("¡No se encontro la ruta de SQLPlus!")
    time.sleep(5)
    exit()

# Inicializar controladores
Raton = MouseController()
Teclado = KeyboardController()

# Funciones
def useMouse(): 
    Raton.press(Button.right)
    Raton.release(Button.right)
    time.sleep(TIME_WAIT_SHORT)
    # Ejecuta el click derecho y luego espera un tiempo.

def useKey():
    Teclado.press(Key.enter)
    Teclado.release(Key.enter)
    time.sleep(TIME_WAIT_LONG)
    # Ejecuta la tecla 'enter' y luego espera un tiempo.

def ejecutarComando(consoleCmd):
    pyperclip.copy(consoleCmd)
    useMouse()
    useKey()
    if consoleCmd == "exit":
        useKey()
    # Utiliza el click derecho y la tecla enter. Si el comando es igual a 'exit' utiliza el enter para cerrar.

def ingresarComando():
    for consoleCmd in listaComandos:
        ejecutarComando(consoleCmd)
    # Trae los comandos de la lista y ejecuta la funcion que los ingresa.

def iniciarConsola():
    os.system(f"start {SQLPlus_Path}")
    time.sleep(TIME_WAIT_LONG)

    ingresarComando()
    # Inicia el programa 'SQLPlus' y luego inicia las funciones de los comandos.