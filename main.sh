# Autores: Tomas Canton y Jon Navarro
# Fecha: 05/04/2023
# Descripcion: Script que permite la ejecucion de los diferentes nodos que permiten realizar la comunicacion
# directa entre los sensores que captan parametros de aire y contaminacion y los terminales que representan
# la media de estos parametros cada 10 segundos
#!/bin/bash

gnome-terminal -- bash -c "python LB_server.py; exec bash"
gnome-terminal -- bash -c "python Data_server.py; exec bash"
sleep 5
for i in {1..20}
do
   python sensores.py
   python sensoresP.py
done  

gnome-terminal -- bash -c "python Terminal_server.py; exec bash"
gnome-terminal -- bash -c "python Terminal_server.py; exec bash"
sleep 10
gnome-terminal -- bash -c "python MeteoProxy.py; exec bash"



