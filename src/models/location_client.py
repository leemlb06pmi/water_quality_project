import requests
import json

class LocationClient:

    def __init__(self, key):
        self.key = key

    def return_lat_long(self,location_city_state):
        #api.openweathermap.org/data/2.5/weather?q=London,uk&APPID=a40848122d57e526e757cb5e98f27ad9
        url = 'http://api.openweathermap.org/geo/1.0/direct?'
        #[city,state] = location_name.split(',')
        search_str = f'{url}q={location_city_state},US&APPID={self.key}'
        response = requests.get(search_str)
        loc = json.loads(response.content)[0]
        return [loc['lat'],loc['lon']]
