import grpc
import numpy as np
from concurrent import futures
import time
from datetime import datetime
from dateutil import parser
import Data_server_pb2
import Data_server_pb2_grpc


from Data_service import Data_service
class Data_serviceServicer(Data_server_pb2_grpc.Data_serviceServicer):

    def process_meteo_data(self, data, context):
        Data_service.process_meteo_data(data)
        response = Data_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def process_pollution_data(self, data, context):
        Data_service.process_pollution_data(self, data)
        response = Data_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
Data_server_pb2_grpc.add_Data_serviceServicer_to_server(Data_serviceServicer(), server)
print('Listening')
server.add_insecure_port('0.0.0.0:50054')
server.add_insecure_port('0.0.0.0:50055')
server.add_insecure_port('0.0.0.0:50056')
server.start()
try:
        while True:
                time.sleep(86400)
except KeyboardInterrupt:
        server.stop(0)

