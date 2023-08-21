import yaml
import sqlalchemy
import psycopg2 as pg2
import pandas as pd
import tabula
import requests
import boto3
from tabula import read_pdf
from sqlalchemy import inspect


class DataExtractor:

    def __init__(self):
        pass

    """ Part 1: Extracting the user data from AWS RDS"""

    def read_db_creds(self):
        with open("db_creds.yaml", 'r') as f:
            creds=yaml.safe_load(f)
            print(creds)
            return creds
            
    def init_db_engine(self):
        creds=self.read_db_creds()
        url = f"postgresql+psycopg2://{creds['RDS_USER']}:{creds['RDS_PASSWORD']}@{creds['RDS_HOST']}:{creds['RDS_PORT']}/{creds['RDS_DATABASE']}"
        engine = sqlalchemy.create_engine(url)
        return engine
        
    def list_db_tables(self):
        connection=self.init_db_engine()
        inspector=inspect(connection)
        table_names=inspector.get_table_names()
        print(f"The table names are{table_names}")
        return table_names


    def read_rds_table(self, pd_name):
        connection=self.init_db_engine()
        table_names=self.list_db_tables()
        pd_name=pd.read_sql_table(table_names[1], connection)
        print(pd_name.columns)
        return pd_name
    
    """Part 2: Extracting card data from pdf"""

    def retrieve_pdf_data(self, link):
        card_df=pd.concat(tabula.read_pdf(link, pages="all"))
        #card_df=df[0]
        return card_df
    
    """Part 3: Extracting details of each store via API """
    
    def API_key(self):
        return {"x-api-key":"yFBQbwXe9J3sd6zWVAMrK6lcxxr0q1lr2PT6DDMX"}

    def list_number_of_stores(self):
        url_API_lists="https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/number_stores"
        response=requests.get(url_API_lists, headers=self.API_key())
        #print('Response status code:', response.status_code)
        print (response.json()['number_stores'])
        return response.json()['number_stores']
        
    def retrieve_store_data(self):
        store_data_frames=[]
        store_number=self.list_number_of_stores()
    
        for i in range(store_number):
            url_API_store_data=f"https://aqj7u5id95.execute-api.eu-west-1.amazonaws.com/prod/store_details/{i}"
            response=requests.get(url_API_store_data, headers=self.API_key())
            data=response.json()
            store_data_frames.append(pd.json_normalize(data))
        store_data=pd.concat(store_data_frames)
        print("Store data extracted successfully")
        return store_data           
        
    """Part 4: Extracting the product details from an S3 bucket"""

    def extract_from_s3(self):
        bucket="data-handling-public"
        file="products.csv"
        
        session=boto3.Session(profile_name="user2")
        s3client=session.client('s3')
        response=s3client.get_object(Bucket=bucket, Key=file)
        
        product_data=pd.read_csv(response["Body"])
        print("Product data extracted successfully")
        return product_data
    
    """Part 5: Extracting the orders table"""

    #Using the same function from part 1
    def read_rds_table_orders(self, pd_name):
        connection=self.init_db_engine()
        table_names=self.list_db_tables()
        pd_name=pd.read_sql_table(table_names[2], connection)
        print(pd_name.columns)
        return pd_name
    
    """Part 6: Extracting date event data from s3 using link"""
    
    def extract_json_from_s3_by_link(self):
        url = 'https://data-handling-public.s3.eu-west-1.amazonaws.com/date_details.json'
        response = requests.get(url) 
        dic = response.json()
        date_data = pd.DataFrame([])
        for column_name in dic.keys():
            value_list = []
            for i in dic[column_name].keys():
                value_list.append(dic[column_name][i])
            date_data[column_name] = value_list
        return date_data
 

test=DataExtractor()
test.list_number_of_stores()