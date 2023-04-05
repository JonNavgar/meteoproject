
import grpc
import numpy as np
from concurrent import futures
import time
from datetime import datetime
from dateutil import parser
import Terminal_server_pb2
import Terminal_server_pb2_grpc
import matplotlib.pyplot as plt
import matplotlib

from Terminal_service import Terminal_service
class Terminal_serviceServicer(Terminal_server_pb2_grpc.Terminal_serviceServicer):

    def send_results(self, CompleteData, context):
        Terminal_service.send_results(CompleteData)
        response = Terminal_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

# Clase Plotter que permite configurar el gráfico 
class Plotter():

    def __init__(self):

        self.x_data = []
        self.y_data = []
        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(12, 6)
        plt.xlabel('Tiempo')
        plt.ylabel('Coef')
        self.line, = self.ax.plot(self.x_data, self.y_data)

    def update(self, x_data, y_data):
        self.x_data = x_data
        print(self.x_data)
        self.y_data = y_data
        print(self.y_data)
        self.line.set_data(self.x_data,self.y_data)

    def plot(self):
        self.ax.relim()
        self.ax.autoscale_view()
        self.fig.canvas.draw()
        plt.pause(1)
        print("updated plot")

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_TerminalServiceServicer_to_server`
# to add the defined class to the server
Terminal_server_pb2_grpc.add_Terminal_serviceServicer_to_server(Terminal_serviceServicer(), server)

# listen on port 50057
print('Starting Terminal_server. Listening on port 50057.')
server.add_insecure_port('0.0.0.0:50057')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
plotter = Plotter()
try:
    while True:
        plotter.update(Terminal_service.x_data, Terminal_service.y_data)
        plotter.plot()

except KeyboardInterrupt:
    server.stop(0)
