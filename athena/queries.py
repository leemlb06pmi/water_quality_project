from datetime import datetime
import awswrangler as wr
from settings import GLUE_DB, S3_PATH


def read_query(query):
    resulting_df = wr.athena.read_sql_query(query, database=GLUE_DB)
    return resulting_df

 
def find_last_end_date(taxpayer_name) -> str:
    df = wr.athena.read_sql_query(
    sql="SELECT max(obligation_end_date) as last_end_date FROM receipts WHERE taxpayer_name=taxpayer_name",
    database=GLUE_DB,
    params={"taxpayer_name": taxpayer_name, "obligation_end_date": "filtered_city"})
    return df.fillna('').last_end_date[0]

#query = "SELECT * FROM receipts where total_receipts > 100 limit 3"