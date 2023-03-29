import meteo_utils
import datetime
from google.protobuf.timestamp_pb2 import Timestamp


class Data_service:
    def process_meteo_data(self, meteo):
        # REDIS -> put (wellness)
        print("Temperatura:", meteo.temperature, "Humedad:", meteo.humidity)
        
        dt = datetime.datetime.fromtimestamp(meteo.datetime.ToSeconds()) 
        print(dt.strftime("%Y-%m-%d %H:%M:%S"))
        
        air_wellness = meteo_utils.MeteoDataProcessor()
        wellness = air_wellness.process_meteo_data(meteo)
        print(wellness)
        
    def process_pollution_data(self, pollut):
        # REDIS ->  put (pollution)
        print('Pollution: ', pollut.co2)
        
        dt = datetime.datetime.fromtimestamp(pollut.datetime.ToSeconds()) 
        print(dt.strftime("%Y-%m-%d %H:%M:%S"))
        
        air_pollution = meteo_utils.MeteoDataProcessor()
        pollution = air_pollution.process_pollution_data(pollut)
        print(pollution)

Data_service = Data_service()

