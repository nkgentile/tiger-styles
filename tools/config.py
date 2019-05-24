import os
from dotenv import load_dotenv
load_dotenv() #TODO add path to .env file inside load_dotenv()

S3_BUCKET   = os.getenv("S3_BUCKET")
S3_KEY      = os.getenv("S3_KEY")
S3_SECRET   = os.getenv("S3_SECRET_ACCESS_KEY")
UPLOAD_FOLDER = os.getenv("TEMP_DIR")

