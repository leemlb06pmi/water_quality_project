import csv
import src.client as clt

client = clt.WaterClient()

records = client.search_basic_results()