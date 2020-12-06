from src.pkg import gmaps
import threading
import time

class GmapsThreading(object):
    def __init__(self, payload, path_result, suffix):
        self.payload = payload
        self.path_result = path_result
        self.suffix = suffix
        thread = threading.Thread(target=self.run, args=())
        thread.daemon = True
        thread.start()

    def run(self):
        try:
            maps_driver = gmaps.setup_maps("https://www.google.com/maps")
            gmaps.maximize_window(maps_driver)
            gmaps.search_place(maps_driver, self.payload["keyword"], self.payload["no_use_category"], self.path_result, self.suffix)
        except Exception as e:
            print("Error:> ", e)
            raise e
            
