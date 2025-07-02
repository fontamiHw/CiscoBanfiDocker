import os

class Config(object):
    
    def __init__(self):
        self.token = "M2IwNDU0OWItYTg1ZC00YjQyLTkwMDMtODQyZDMyYzA1M2U2NmQ1MjdlOTktNWFi_PF84_1eb65fdf-9643-417f-9974-ad72cae0e10f"
        self.name = "MikExperiment"
        self.uniqueId = "Y2lzY29zcGFyazovL3VzL0FQUExJQ0FUSU9OLzI5ODFhMjhjLTQ0MTUtNDcwMy1iOWRjLTViNmJlNzlkNjg0MQ"
        self.proxies = os.environ.get("HTTP_PROXY", None)
        self.open_route = "/data/host/SOR/"
        self.save_route_svg = "/data/host/SVG/"
        self.save_route_jpg= "/data/host/JPG/"

    def get_token(self):
        return self.token

    def get_name(self):
        return self.name

    def get_uniqueId(self):
        return self.uniqueId  

    def get_proxies(self):
        return self.proxies
    
    def get_open_route(self):
        return self.open_route
    
    def get_save_route_svg(self):
        return self.save_route_svg
    
    def get_save_route_jpg(self):
        return self.save_route_jpg
