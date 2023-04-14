
import grpc
import numpy as np
from concurrent import futures
import time
from datetime import datetime
from dateutil import parser
import LB_server_pb2
import LB_server_pb2_grpc
import grpc.aio


from LB_service import LB_service
class LB_serviceServicer(LB_server_pb2_grpc.LB_serviceServicer):

    def send_meteo_data(self, data, context):
        LB_service.send_meteo_data(data)
        response = LB_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

    def send_pollution_data(self, data, context):
        LB_service.send_pollution_data(data)
        response = LB_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_LBServiceServicer_to_server`
# to add the defined class to the server
LB_server_pb2_grpc.add_LB_serviceServicer_to_server(LB_serviceServicer(), server)

# listen on port 50051
print('Starting LB_server. Listening on port 50051.')
server.add_insecure_port('0.0.0.0:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)

