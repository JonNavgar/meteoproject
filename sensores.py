import grpc
import google
import meteo_utils
# import the generated classes
from google.protobuf import timestamp_pb2
import LB_server_pb2
import LB_server_pb2_grpc
import time

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')
print("Sensor de aire")

time1 = google.protobuf.timestamp_pb2.Timestamp()

# create a stub (client)
stub1 = LB_server_pb2_grpc.LB_serviceStub(channel)
air = meteo_utils.MeteoDataDetector()
meteo_data = air.analyze_air()
time1.GetCurrentTime()
raw_meteo = LB_server_pb2.RawMeteoData(temperature=meteo_data.get("temperature"),humidity=meteo_data.get("humidity"),datetime=time1)
stub1.send_meteo_data(raw_meteo)

