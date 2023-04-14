import redis
import time
from datetime import datetime, timedelta
import grpc
import Terminal_server_pb2
import Terminal_server_pb2_grpc

# Conexión Redis
r_client = redis.StrictRedis(host="localhost", port=6379, password="", decode_responses=True)
Y = 3
while True:
    # WELLNESS
    w_list = []
    w_string = r_client.lpop("wellness")
    if w_string is None:
        print("No hay datos wellness")
        while True:
            time.sleep(Y)
            w_string = r_client.lpop("wellness")
            if w_string is not None:
                break

    w_first = datetime.strptime(w_string.strip('()').split(" : ")[0], "%Y-%m-%d %H:%M:%S")
    w_limit = w_first + timedelta(seconds=Y)
    w_list.append(float(w_string.strip('()').split(" : ")[1]))
    while True:
        w_string = r_client.lpop("wellness")
        if w_string is None:
            break

        w_time = datetime.strptime(w_string.strip('()').split(" : ")[0], "%Y-%m-%d %H:%M:%S")
        if w_limit < w_time:
            break

        w_list.append(float(w_string.strip('()').split(" : ")[1]))

    w_avg = round(sum(w_list) / len(w_list), 3)

    # POLLUTION
    p_list = []
    p_string = r_client.lpop("pollution")
    if p_string is None:
        print("No hay datos pollution")
        while True:
            time.sleep(Y)
            p_string = r_client.lpop("pollution")
            if p_string is not None:
                break

    p_first = datetime.strptime(p_string.strip('()').split(" : ")[0], "%Y-%m-%d %H:%M:%S")
    p_limit = p_first + timedelta(seconds=Y)
    p_list.append(float(p_string.strip('()').split(" : ")[1]))

    while True:
        p_string = r_client.lpop("pollution")
        if p_string is None:
            break

        p_time = datetime.strptime(p_string.strip('()').split(" : ")[0], "%Y-%m-%d %H:%M:%S")
        if p_limit < p_time:
            break

        p_list.append(float(p_string.strip('()').split(" : ")[1]))

    p_avg = round(sum(p_list) / len(p_list), 3)

    # Enviar a las terminales las medias cada Y segundos
    # Crear cliente y rellenar mensaje de rpc
    channel = grpc.insecure_channel('localhost:50057')
    stub1 = Terminal_server_pb2_grpc.Terminal_serviceStub(channel)
    # Para wellness data
    complete_data = Terminal_server_pb2.CompleteData()
    complete_data.wellness = w_avg
    w_time_str = w_time.strftime("%Y-%m-%d %H:%M:%S")
    complete_data.datetimew = w_time_str
    # Para pollution data
    complete_data.pollution = p_avg
    p_time_str = p_time.strftime("%Y-%m-%d %H:%M:%S")
    complete_data.datetimep = p_time_str
    stub1.send_results(complete_data)
    # Wait for Y seconds	
    time.sleep(Y)


