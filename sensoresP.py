import grpc
import google
import meteo_utils
# import the generated classes
from google.protobuf import timestamp_pb2
import LB_server_pb2
import LB_server_pb2_grpc

# open a gRPC channel
channel = grpc.insecure_channel('localhost:50051')

print("Sensor de contaminacion")

# create a stub (client1)
stub1 = LB_server_pb2_grpc.LB_serviceStub(channel)
pollution = meteo_utils.MeteoDataDetector()
pollution_data = pollution.analyze_pollution()
time = google.protobuf.timestamp_pb2.Timestamp()
time.GetCurrentTime()
raw_pollution = LB_server_pb2.RawPollutionData(co2=pollution_data.get("co2"),datetime=time)
stub1.send_pollution_data(raw_pollution)


