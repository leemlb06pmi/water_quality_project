import requests
import json
import src.adapter as ad

class WaterClient:
    def search_basic_results(self, location):
        url = 'https://www.waterqualitydata.us/data/Result/search?'
        loc = f'lat={round(location[0],1)}&long={round(location[1],1)}&within=25.0'
        characteristic = 'characteristicName=Lead'
        output = 'mimeType=csv'
        #compression = 'zip=yes'
        url_list = [loc,characteristic,output]
        search_str = url+'&'.join(url_list)
        response = requests.get(search_str)
        adapter = ad.Adapter()
        decoded_response = response.content.decode('utf-8')
        records = adapter.open_decoded_csv(decoded_response)
        return [record for record in records if record.ResultMeasureValue != '']
    
    def create_dfs(self, records):
        adapter = ad.Adapter()
        return adapter.build_df(records)


