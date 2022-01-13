class Service:
    @staticmethod
    def ulr_identification(user_data):
        url = user_data["url"]
        return url

    @staticmethod
    def location(user_data):
        lat = user_data["lat"]
        lon = user_data["lon"]
        return lat, lon
