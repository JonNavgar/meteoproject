import grpc
import google
import meteo_utils
# import the generated classes
from google.protobuf import timestamp_pb2
import Data_server_pb2
import Data_server_pb2_grpc

class LB_service:
    def __init__(self):
        self.servers = [
            ('0.0.0.0', '50051'),
            ('0.0.0.0', '50052'),
            ('0.0.0.0', '50053')
        ]
        self.server_index = 0
    def send_meteo_data(self, meteo):
	# Round Robin
        selected_server = self.servers[self.server_index % len(self.servers)]
        self.server_index = self.server_index + 1
	# Crear cliente
        channel = grpc.insecure_channel(f"{selected_server[0]}:{selected_server[1]}")
        stub = Data_server_pb2_grpc.Data_serviceStub(channel)
	# LLamar a la RPC (process_meteo) del proto del server
        stub.process_meteo_data(meteo)
    def send_pollution_data(self, pollut):
        # Round Robin
        selected_server = self.servers[self.server_index % len(self.servers)]
        self.server_index = self.server_index + 1
        # Crear cliente
        channel = grpc.insecure_channel(f"{selected_server[0]}:{selected_server[1]}")
        stub = Data_server_pb2_grpc.Data_serviceStub(channel)
        # LLamar a la RPC (process_pollution) del proto del server
        stub.process_pollution_data(meteo)

LB_service = LB_service()
