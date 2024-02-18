import os
from dotenv import load_dotenv

load_dotenv()

LOCATION_KEY = os.environ["LOCATION_API_KEY"]
DB_NAME = os.environ["DB_NAME"]
DB_HOST = os.environ["DB_HOST"]
S3_PATH = os.environ["S3_PATH"]
GLUE_DB = os.environ["GLUE_DB"]
