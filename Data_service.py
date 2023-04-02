import meteo_utils
import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import redis


redis_host = "localhost"
redis_port = 6379
redis_password = ""

r_client = redis.StrictRedis(host=redis_host, port=redis_port, password=redis_password, decode_responses=True)
        

class Data_service:
    def process_meteo_data(self, meteo):
        #print("Temperatura:", meteo.temperature, "Humedad:", meteo.humidity)
        
        dt = datetime.datetime.fromtimestamp(meteo.datetime.ToSeconds()) 
        
        air_wellness = meteo_utils.MeteoDataProcessor()
        wellness = air_wellness.process_meteo_data(meteo)
        
        key = dt.strftime("%Y-%m-%d %H:%M:%S")
        
        r_client.rpush('wellness', f'({dt.strftime("%Y-%m-%d %H:%M:%S")} : {wellness})')
        #r_client.zadd('wellness',{key : wellness}) Lista ordenada no necesaria
        #redis-cli en terminal y keys *, hgetall 
        

        
    def process_pollution_data(self, pollut):
        
        dt = datetime.datetime.fromtimestamp(pollut.datetime.ToSeconds()) 
        
        air_pollution = meteo_utils.MeteoDataProcessor()
        pollution = air_pollution.process_pollution_data(pollut)
        
        key = dt.strftime("%Y-%m-%d %H:%M:%S")
        r_client.rpush('pollution', f'({dt.strftime("%Y-%m-%d %H:%M:%S")} : {pollution})')
        #r_client.set(key,pollution)



Data_service = Data_service()

