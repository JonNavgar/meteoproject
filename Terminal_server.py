
import grpc
import numpy as np
from concurrent import futures
import time
from datetime import datetime
from dateutil import parser
import Terminal_server_pb2
import Terminal_server_pb2_grpc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
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

        self.xw_data = []
        self.yw_data = []
        self.xp_data = []
        self.yp_data = []
        self.fig, self.ax = plt.subplots()
        self.fig.set_size_inches(12, 6)
        plt.xlabel('Tiempo')
        plt.ylabel('Media Coef')
        plt.title('Wellness vs Pollution')
        date_fmt = '%Y-%m-%d %H:%M:%S'
        date_formatter = mdates.DateFormatter(date_fmt)
        self.ax.xaxis.set_major_formatter(date_formatter)
        self.line1, = self.ax.plot(self.xw_data, self.yw_data, color='blue', label='wellness')
        self.line2, = self.ax.plot(self.xp_data, self.yp_data, color='red', label='pollution')

    def update(self, xw_data, yw_data, xp_data, yp_data):
        self.xw_data = xw_data
        self.yw_data = yw_data
        self.xp_data = xp_data
        self.yp_data = yp_data
        self.line1.set_data(self.xw_data,self.yw_data)
        self.line2.set_data(self.xp_data,self.yp_data)

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
        plotter.update(Terminal_service.xw_data, Terminal_service.yw_data, Terminal_service.xp_data, Terminal_service.yp_data)
        plotter.plot()

except KeyboardInterrupt:
    server.stop(0)
