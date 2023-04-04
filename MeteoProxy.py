import redis
import time
import Terminal_server_pb2
import Terminal_server_pb2_grpc
import grpc
import datetime
# Connect to Redis server
print("Proxy")
r = redis.Redis(host='localhost', port=6379, db=0)
Y = 30 
wellness_values = []
#Ciclo infinito para leer datos de Redis 
while True: 
	#Obtener lista de datos de Redis
	wellness_data = r.lrange('wellness', 0, -1)
	pollution_data = r.lrange('pollution', 0, -1)
	for element in wellness_data: 
		element_str = element.decode('utf-8')
		#Separamos los elementos del diccionario 
		tiempo, wellness_str = element_str.strip('()').split(" : ")
		#String convertido a float 
		wellness = float(wellness_str.strip())
		wellness_values.append(wellness)
		if len(wellness_values) > 0: 
			wellness_mean = sum(wellness_values) / len(wellness_values)
			#pollution_mean = sum(pollution_values) / len(pollution_data)
	# Enviar a las terminales las medias cada Y segundos
	# Crear cliente y rellenar mensaje de rpc
	channel = grpc.insecure_channel('localhost:50057')
	stub1 = Terminal_server_pb2_grpc.Terminal_serviceStub(channel)
	# Para wellness data
	wellness_data = Terminal_server_pb2.WellnessData()
	wellness_data.wellness = wellness_mean
	wellness_data.datetime = tiempo
	complete_data = Terminal_server_pb2.CompleteData()
	complete_data.wellness.CopyFrom(wellness_data)
	# Para pollution data
	#pollution_data = Terminal_server_pb2.PollutionData()
        #pollution_data.wellness = pollution_mean
        #pollution_data.datetime = tiempo
        #pollution_data = Terminal_server_pb2.CompleteData()
        #complete_data.wellness.CopyFrom(pollution_data)
	stub1.send_results(complete_data)
	# Wait for Y seconds	
	time.sleep(Y)
