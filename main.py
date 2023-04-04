# Autores: Tomas Canton y Jon Navarro
# Fecha: 05/04/2023
# Descripcion: Script que permite la ejecucion de los diferentes nodos que permiten realizar la comunicacion
# directa entre los sensores que captan parametros de aire y contaminacion y los terminales que representan
# la media de estos parametros cada 10 segundos
import subprocess
import time 
subprocess.Popen(['xterm', '-e', 'python', 'LB_server.py'])
time.sleep(3)
subprocess.Popen(['xterm', '-e', 'python', 'Data_server.py'])
time.sleep(3)
subprocess.Popen(['xterm', '-e', 'python', 'Terminal_server.py'])
time.sleep(20)
subprocess.Popen(['xterm', '-e', 'python', 'MeteoProxy.py'])
time.sleep(3)
subprocess.Popen(['xterm', '-e', 'python', 'sensores.py'])
time.sleep(10)
subprocess.Popen(['xterm', '-e', 'python', 'sensores.py'])
time.sleep(10)
subprocess.Popen(['xterm', '-e', 'python', 'sensoresP.py'])
time.sleep(10)
subprocess.Popen(['xterm', '-e', 'python', 'sensoresP.py'])




