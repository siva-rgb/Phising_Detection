import os
import sys
import certifi
import pymongo

from src.constants import *
from src.exception import CustomException


cs= certifi.where()

class MongoDBClient:
    client= None
    
    def __init__(self,database_name= DATABASE_NAME):
        try:
            if MongoDBClient.client is None:
                mongo_db_url= os.get_en("MONGO_DB_URL")
                if mongo_db_url is None:
                    raise Exception("Enerioment key: MONGO_DB_URL is not set")
                MongoDBClient.client= pymongo.MongoClient(mongo_db_url,tls=True, tlsCAFile=cs)
            self.client= MongoDBClient.client
            self.database= self.client(database_name)
            self.database_name= database_name
            
        except Exception as e:
            raise CustomException(e,sys)
              

