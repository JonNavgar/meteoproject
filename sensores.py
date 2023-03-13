import grpc
import meteo_utils
from google.protobuf import timestamp_pb2
# import the generated classes
import LB_server_pb2
import LB_server_pb2_grpc
# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

# create a couple of stubs (client)
stub1 = LB_server_pb2_grpc.LB_serviceStub(channel)
stub2 = LB_server_pb2_grpc.LB_serviceStub(channel)

air = meteo_utils.MeteoDataDetector()
meteo_data = air.analyze_air()
time = timestamp_pb2.Timestamp.GetCurrentTime()
raw_meteo = LB_server_pb2.RawMeteoData(temperature=meteo_data.get("temperature"),humidity=meteo_data.get("humidity"),datetime=time)
stub1.send_meteo_data(raw_meteo)
