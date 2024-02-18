import csv
import src.models as models
from settings import LOCATION_KEY
from aws_utils import delete_from_s3, write_to_s3, read_from_s3
from athena.migrations import create_db, crawl_dataset, databases

loc_client = models.LocationClient(LOCATION_KEY)
location_str = 'Nashville, tn'
#[city,state] = location_str.split(', ')
location = loc_client.return_lat_long(location_str)

water_client = models.WaterClient()
records = water_client.search_basic_results(location)
df = water_client.create_dfs(records)
delete_from_s3()
write_to_s3(df, location_str.split(',')[0])
#create_db()
crawl_dataset(location_str)




