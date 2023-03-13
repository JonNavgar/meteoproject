
import grpc
from concurrent import futures
from datetime import datetime
from dateutil import parser
import LB_server_pb2
import LB_server_pb2_grpc

from LB_service import LB_service
class LB_ServiceServicer(LB_server_pb2_grpc.LB_ServiceServicer):
    def send_meteo_data(self, data, context):
        response = LB_service.send_meteo_data(self, data)
        #Puede ser que haya que hacer con el proto (pb2) para actualizar los mensajes de vuelta al cliente
        return response
    def send_pollution_data(self,data,context):
        response = LB_service.send_pollution_data(self, data)
        #Puede ser que haya que hacer con el proto (pb2) para actualizar los mensajes de vuelta al cliente
        return response
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
LB_server_pb2_grpc.add_LB_serviceServicer_to_server(LB_ServiceServicer(), server)
print('Starting server. Listening on port 50051.')
server.add_insecure_port('0.0.0.0:50051')
server.start()