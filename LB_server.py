
import grpc
from concurrent import futures
import time
from datetime import datetime
from dateutil import parser
import LB_server_pb2
import LB_server_pb2_grpc

from LB_service import LB_service
class LB_ServiceServicer(LB_server_pb2_grpc.LB_ServiceServicer):
    def send_meteo_data(self, data, context):
        # Hay que pasarle el parametro data separando las variables o junto?
        LB_service.send_meteo_data(data.temperature, data.humidity, data.datetime)
        response = LB_Server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response
    def send_pollution_data(self, data, context):
        LB_service.send_pollution_data(self, data.co2, data.datetime)
        response = LB_Server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
LB_server_pb2_grpc.add_LB_serviceServicer_to_server(LB_ServiceServicer(), server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('0.0.0.0:50051')
server.start()