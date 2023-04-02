import grpc
import google
# import the generated classes
import Terminal_server_pb2
import Terminal_server_pb2_grpc

class Terminal_service:
        
    def send_results(self, data):
	# Imprimir valores con colores o grafico en tiempo real
        print(data.wellness.wellness)
        print(data.wellness.datetime)
Terminal_service = Terminal_service()
