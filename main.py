
import pandas as pd
from data_extraction import DataExtractor
from data_cleaning import DataCleaning
from database_utils import DatabaseConnector

de=DataExtractor()
dc=DataCleaning()
db=DatabaseConnector()

"""Part 1: Extracting, cleaning and uploading user data to our database"""
def upload_user_data():
    user_data=de.read_rds_table(pd_name="user_data")
    dc.clean_user_data(user_data)
    db.upload_to_db(user_data, "dim_users")
    print("User data uploaded successfully")

"""Part 2: Extracting, cleaning and uploading card data to our database"""
def upload_card_data():
    card_data=de.retrieve_pdf_data(link="https://data-handling-public.s3.eu-west-1.amazonaws.com/card_details.pdf")
    dc.clean_card_data(card_data)
    db.upload_to_db(card_data, "dim_card_details")
    print("Card data uploaded successfully")
    

"""Part 3: Extracting, cleaning and uploading store data to our database"""
def upload_store_data():
    store_data=de.retrieve_store_data()
    store_data=store_data.drop(["lat"], axis=1)
    print(store_data.head(5))
    dc.cleaning_store_data(store_data)
    db.upload_to_db(store_data, "dim_store_details")
    print("Store data uploaded successfully")

"""Part 4: Extracting, cleaning and uploading product data to our database"""
def upload_product_data():
    product_data=de.extract_from_s3()
    dc.convert_product_weights(product_data)
    dc.clean_products_data(product_data)
    db.upload_to_db(product_data, "dim_products")
    print("Product data uploaded successfully")

"""Part 5: Extracting, cleaning and uploading order data to our database"""
def upload_order_data():
    order_data=de.read_rds_table_orders(pd_name="order_data")
    dc.clean_orders_table(order_data)
    order_data=order_data.drop(["level_0", "first_name", "last_name", "1"], axis=1)
    db.upload_to_db(order_data, "orders_table")
    print("Order data uploaded successfully")


"""Part 6: Extracting, cleaning and uploading event date date to our database"""
def upload_date_data():
    date_data=de.extract_json_from_s3_by_link()
    date_data=dc.clean_date_time(table=date_data)
    db.upload_to_db(date_data, "dim_date_times")
    print("Date event data uploaded successfully")


upload_user_data()
upload_card_data()
upload_product_data()
upload_order_data()
upload_store_data()
upload_date_data()

