import meteo_utils
class LB_service:
    def send_meteo_data(self, request):
        air = meteo_utils.MeteoDataProcessor()
        processed_data = air.process_meteo_data(self, request)
    def send_pollution_data(self, request):
        pollution = meteo_utils.MeteoDataProcessor()
        processed_pollution = pollution.process_pollution_data(self, request)

    LB_service = LB_service()