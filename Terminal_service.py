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
    #def __init__(self):
        # Crear el plot
        # self.x_data = []
        # self.y_data = []
        # self.fig, self.ax = plt.subplots()
        # self.fig.set_size_inches(12,6)
        # Configurar el formato de las fechas en el eje y
        #date_format = '%Y-%m-%d %H:%M:%S'
        #plt.gca().xaxis.set_major_formatter(plt.FixedFormatter([]))
        #plt.gca().yaxis.set_major_formatter(plt.FuncFormatter(lambda x, pos: dt.datetime.fromtimestamp(x).strftime(date_format)))
        # Configurar etiqueta eje x y eje y
        #plt.xlabel('Tiempo')
        #plt.ylabel('Media coeficientes')
        # Crear plot inicial
        #self.line, = self.ax.plot(self.x_data, self.y_data)
    def send_results(self, data):
        print(data.wellness.wellness)
        # Actualizar plot
        #x = dt.datetime.strptime(data.wellness.datetime, '%Y-%m-%d %H:%M:%S')
        #y = data.wellness.wellness
        #self.x_data.append(x)
        #self.y_data.append(y)
        #self.line.set_data(self.x_data, self.y_data)
        #self.ax.set_xlim([max(0, x.timestamp() - 30),x.timestamp()])
        #self.fig.canvas.draw()
        #plt.show()
Terminal_service = Terminal_service()
