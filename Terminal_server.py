
import grpc
import numpy as np
from concurrent import futures
import time
from datetime import datetime
from dateutil import parser
import Terminal_server_pb2
import Terminal_pb2_grpc


from Terminal_service import Terminal_service
class Terminal_serviceServicer(Terminal_server_pb2_grpc.Terminal_serviceServicer):

    def send_results(self, CompleteData context):
        Terminal_service.send_results(CompleteData)
        response = Terminal_server_pb2.google_dot_protobuf_dot_empty__pb2.Empty()
        return response

# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_InsultingServiceServicer_to_server`
# to add the defined class to the server
Terminal_server_pb2_grpc.add_Terminal_serviceServicer_to_server(Terminal_serviceServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('0.0.0.0:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
