import redis
import time


# Connect to Redis server
r = redis.Redis(host='localhost', port=6379, db=0)


Y = 30 
wellness_values = []


#Ciclo infinito para leer datos de Redis 
while True: 
	#Obtener lista de datos de Redis
	wellness_data = r.lrange('wellness', 0, -1)
	pollution_data = r.lrange('pollution', 0, -1)
	
	print('Wellness:', wellness_data, '\nPollution:', pollution_data)
	
	for element in wellness_data: 
		element_str = element.decode('utf-8')
		print(element, element_str)
		
		#Separamos los elementos del diccionario 
		tiempo, wellness_str = element_str.strip('()').split(" : ")
		
		#String convertido a float 
		wellness = float(wellness_str.strip())
		wellness_values.append(wellness)
		print(f"Clave: {tiempo.strip()}\n valor: {wellness}")
		
		if len(wellness_values) > 0: 
			wellness_mean = sum(wellness_values) / len(wellness_values)
			#pollution_mean = sum(pollution_values) / len(pollution_data)
	
	print(f'Wellness mean: {wellness_mean}')
	
	
	# Wait for Y seconds	
	time.sleep(Y)
