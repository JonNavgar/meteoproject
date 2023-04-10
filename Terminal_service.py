import grpc
import google
# import the generated classes
import Terminal_server_pb2
import Terminal_server_pb2_grpc
import matplotlib.pyplot as plt
import matplotlib
import datetime as dt

class Terminal_service:
    # Imprimir valores con colores o grafico en tiempo real
    def __init__(self):
        # Crear el plot
         self.xw_data = []
         self.yw_data = []
         self.xp_data = []
         self.yp_data = []
    def send_results(self, data):
        print("resultado enviado")
        # Actualizar plot
	# Wellness
        x_datetimew = dt.datetime.strptime(data.datetimew, '%Y-%m-%d %H:%M:%S')
        xw = x_datetimew
        yw = data.wellness
        self.xw_data.append(xw)
        self.yw_data.append(yw)
	# Pollution 
        x_datetimep = dt.datetime.strptime(data.datetimep, '%Y-%m-%d %H:%M:%S')
        xp = x_datetimep
        yp = data.pollution
        self.xp_data.append(xp)
        self.yp_data.append(yp)

Terminal_service = Terminal_service()
