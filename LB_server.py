
import grpc
import numpy as np
from concurrent import futures
import time
from datetime import datetime
from dateutil import parser
import LB_server_pb2
import LB_server_pb2_grpc


from LB_service import LB_service
class LB_serviceServicer(LB_server_pb2_grpc.LB_serviceServicer):

    def send_meteo_data(self, data, context):
        LB_service.send_meteo_data(data)
        response = LB_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def send_pollution_data(self, data, context):
        LB_service.send_pollution_data(self, data)
        response = LB_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
LB_server_pb2_grpc.add_LB_serviceServicer_to_server(LB_serviceServicer(), server)
