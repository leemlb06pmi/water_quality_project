import requests
import src.adapter as ad

class WaterClient:
    def search_basic_results(self):
        url = 'https://www.waterqualitydata.us/data/Result/search?'
        county_specific_search = 'countycode=US%3A47%3A157'
        characteristic = 'characteristicName=Lead'
        output = 'mimeType=csv'
        #compression = 'zip=yes'
        url_list = [county_specific_search,characteristic,output]
        search_str = url+'&'.join(url_list)
        response = requests.get(search_str)
        adapter = ad.Adapter()
        decoded_response = response.content.decode('utf-8')
        records = adapter.open_decoded_csv(decoded_response)
        return [record for record in records if record.ResultMeasureValue != '']

