import os
from datetime import datetime

AWS_S3_BUCKET_NAME="siva-phishingdetection"
TARGET_COLUMN="Result"
DATABASE_NAME= "phishing"
MODEL_FILE_NAME="model"
MODEL_FILE_EXTENTION=".pkl"
artifact_folder_name = datetime.now().strftime('%m_%d_%Y_%H_%M_%S')
artifact_folder = os.path.join("artifacts", artifact_folder_name)