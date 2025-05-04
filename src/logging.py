import logging
from datetime import datetime
import os

# log file name
LOG_FILE= f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# path where file will be saved
logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

# create log folder if already not exsist
os.makedirs(logs_path, exist_ok=True)

# get the already saved log file
LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

# write the logs from the code to this log file
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)