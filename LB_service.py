import meteo_utils
class LB_service:
    def __init__(self):
        self.servers = [
            ('192.168.1.1', '50051'),
            ('192.168.1.2', '50051'),
            ('192.168.1.3', '50051')
        ]
        self.server_index = 0
    def send_meteo_data(self, temperature, humidity, time):
        # Crear cliente
        # LLamar a la RPC del proto del server
        # Round Robin
        server = self.servers[self.server_index]
        self.server_index = (self.server_index + 1) % len(self.servers)
        # LLamar a process_meteo_data
    def send_pollution_data(self, co2, time):
        pollution = meteo_utils.MeteoDataProcessor()
        processed_pollution = pollution.process_pollution_data(self, request)

    LB_service = LB_service()