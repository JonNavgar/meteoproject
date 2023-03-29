import meteo_utils
import datetime
from google.protobuf.timestamp_pb2 import Timestamp


class Data_service:
    def process_meteo_data(self, meteo):
        # REDIS -> put (wellness)
        print("Temperatura:", meteo.temperature, "Humedad:", meteo.humidity)
        
        dt = datetime.datetime.fromtimestamp(meteo.datetime.ToSeconds()) 
        print(dt.strftime("%Y-%m-%d %H:%M:%S"))
        
    def process_pollution_data(self, pollut):
        # REDIS ->  put (pollution)
        print('He llegau')

Data_service = Data_service()

