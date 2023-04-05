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
         self.x_data = []
         self.y_data = []
    def send_results(self, data):
        print(data.wellness.wellness)
        # Actualizar plot
        # x = dt.datetime.strptime(data.wellness.datetime, '%Y-%m-%d %H:%M:%S')
        x = data.wellness.datetime
        y = data.wellness.wellness
        self.x_data.append(x)
        self.y_data.append(y)

Terminal_service = Terminal_service()
