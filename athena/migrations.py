import awswrangler as wr
from settings import GLUE_DB, S3_PATH

databases = wr.catalog.databases()

def create_db():
    wr.catalog.create_database(GLUE_DB)

def delete_db(GLUE_DB):
    wr.catalog.delete_database(
        name=GLUE_DB
    )

def crawl_dataset(location):
    [city,state]=location.split(',')
    state = state.lstrip().upper()
    res = wr.s3.store_parquet_metadata(
        #path=f'{S3_PATH}Nashville*.parquet',
        path = 's3://water-reports/Nashville*.parquet',
        database=GLUE_DB,
        table=f'{city}-{state}',
        dataset=True,
        mode="overwrite")
    
    
def display_schema(table_name):
    return wr.catalog.table(database=GLUE_DB, table=table_name)