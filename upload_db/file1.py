from pymongo import MongoClient
import pandas as pd
import os

mongo_uri= 'mongodb+srv://sivananda:mongo123@cluster0.dudjfbj.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'

database_name= 'phishing'
client= MongoClient(mongo_uri)
collection_name= None
file_path= 'phising_08012020_120000.csv'
if file_path.endswith('.csv'):
    collection_name= file_path.split('.')[0]
df= pd.read_csv('phising_08012020_120000.csv')
print('Hello',collection_name)
#print(df.head(2))

#adding data to db
db= client[database_name]
collection= db[collection_name]

data= df.to_dict(orient='records')
collection.insert_many(data)
print('data loaded sucessfully')