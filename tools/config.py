import os
from dotenv import load_dotenv
load_dotenv()  # TODO add path to .env file inside load_dotenv()

# AWS S3 Configuration
S3_BUCKET = os.getenv("S3_BUCKET")
S3_KEY = os.getenv("S3_KEY")
S3_SECRET = os.getenv("S3_SECRET_ACCESS_KEY")

# Project Configuration
PROJECT_ROOT = os.getcwd()

UPLOAD_FOLDER = "{}/uploads".format(PROJECT_ROOT)

CONTENT_FOLDER = "{}/content".format(UPLOAD_FOLDER)
if (not os.path.isdir(CONTENT_FOLDER)):
    os.makedirs(CONTENT_FOLDER)

STYLED_FOLDER = "{}/styled".format(UPLOAD_FOLDER)
if (not os.path.isdir(STYLED_FOLDER)):
    os.makedirs(STYLED_FOLDER)

MODELDIR = '{}/xform'.format(PROJECT_ROOT)
