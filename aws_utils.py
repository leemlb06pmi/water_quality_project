import awswrangler as wr
from settings import S3_PATH

def delete_from_s3():
    wr.s3.delete_objects(S3_PATH)

def write_to_s3(df, city, mode = 'overwrite'):
    wr.s3.to_parquet(df=df,
                    path=S3_PATH,
                    filename_prefix=city,
                    mode=mode, dataset = True
                    )

def read_from_s3():
    df = wr.s3.read_parquet(S3_PATH, dataset=True)
    return df