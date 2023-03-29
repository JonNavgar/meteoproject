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


time1 = google.protobuf.timestamp_pb2.Timestamp()

# create a stub (client 1)
stub1 = LB_server_pb2_grpc.LB_serviceStub(channel)
air = meteo_utils.MeteoDataDetector()
meteo_data = air.analyze_air()
time1.GetCurrentTime()
raw_meteo = LB_server_pb2.RawMeteoData(temperature=meteo_data.get("temperature"),humidity=meteo_data.get("humidity"),datetime=time1)
stub1.send_meteo_data(raw_meteo)


#Crear stub 2 (client 2)
time.sleep(1)

stub2 = LB_server_pb2_grpc.LB_serviceStub(channel)
air2 = meteo_utils.MeteoDataDetector()
meteo_data2 = air2.analyze_air()
time2 = google.protobuf.timestamp_pb2.Timestamp()
time2.GetCurrentTime()
raw_meteo2 = LB_server_pb2.RawMeteoData(temperature=meteo_data2.get("temperature"),humidity=meteo_data2.get("humidity"),datetime=time2)
stub2.send_meteo_data(raw_meteo2)
