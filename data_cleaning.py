import pandas as pd
import numpy as np
import re


class DataCleaning:

    def __init__(self):
        pass

    """Part 1: Cleaning the user data"""

    def clean_user_data(self,table):
        #Formatting the dates correctly
        table=self.date_format_2(table=table, column_name="date_of_birth")
        table=self.date_format_2(table=table, column_name="join_date")
        table=self.clean_email(table=table)
        #Removing any null values
        #table=table.dropna(axis='index', how='any',inplace=True)
        return table

    """Part 2: Cleaning the card data """
    def clean_card_data(self,table):
        #Ensuring that the card numbers only contain digits
        table['card_number'].apply(self.isDigit)
        #Formatting the date
        table=self.date_format_2(table=table, column_name="date_payment_confirmed")
        table=table.dropna(axis='index', how='any',inplace=True)
        return table

    """Part 3: Cleaning the store data """
    
    def cleaning_store_data(self, table):
        table=self.date_format(table=table, column_name="opening_date")                    
        table['staff_numbers'] =  pd.to_numeric( table['staff_numbers'].apply(self.remove_char_from_string),errors='coerce', downcast="integer") 
        table.dropna(subset = ['staff_numbers'],how='any',inplace= True)
        return table

    def remove_char_from_string(self,value):
        return re.sub(r'\D', '',value) 
    
    """Part 4: Cleaning the product data"""
    def convert_product_weights(self,table):
        table["weight"]=table["weight"].apply(self.convert_to_kg)
        table=table.dropna(axis='index', how='any', inplace=True)
        print("Weights converted successfully")
       
    def clean_products_data(self,table):
        #Ensuring the date the product was added is formatted correctly
        table=self.date_format(table=table, column_name="date_added")
        return table
    
    """Part 5: Cleaning the orders table"""
    def clean_orders_table(self, table):
        table.drop(["first_name", "last_name", "1"], axis=1)
        return table
    
    """Part 6: Cleaning event date table"""
    def clean_date_time(self,table):
        table['month'] =  pd.to_numeric( table['month'],errors='ignore', downcast="integer")
        table['year'] =  pd.to_numeric( table['year'], errors='ignore', downcast="integer")
        table['day'] =  pd.to_numeric( table['day'], errors='ignore', downcast="integer")
        table.dropna(how='any',inplace= True)      
        return table

        """Index of functions used to clean the data"""
    
    def clean_email(self, table):
        if '@' in table["email_address"]:
            return table["email_address"]
        else: 
            return np.nan
    
    def date_format(self, table, column_name):
        table[column_name] = pd.to_datetime(table[column_name], errors='ignore')
        table.dropna(axis=0, how='any',inplace= True)
        return table
    
    def date_format_2(self, table, column_name):
        table[column_name] = pd.to_datetime(table[column_name], format='%Y-%m-%d', errors='ignore')
        table[column_name] = pd.to_datetime(table[column_name], format='%Y %B %d', errors='ignore')
        table[column_name] = pd.to_datetime(table[column_name], format='%B %Y %d', errors='ignore')
        table[column_name] = pd.to_datetime(table[column_name], errors='coerce')
        table.dropna(subset = column_name,how='any',inplace= True)
        return table


    def removing_string(self, s):
        return re.sub(r'\d+', '', s)

    def convert_to_kg(self, w):
       w=str(w)
       if w.endswith("kg"):
            w=w.replace("kg", " ")
            w=self.perform_calc(w)
            return w
       elif w.endswith("g"):
            w=w.replace("g", " ")
            w=self.perform_calc(w)
            return (float(w))/1000 if self.isfloat(w) else np.nan
       elif w.endswith("g ."):
            w=w.replace("g .", " ")
            w=self.perform_calc(w)
            return (float(w))/1000 if self.isfloat(w) else np.nan
       elif w.endswith("ml"):
            w=w.replace("ml", " ")
            w=self.perform_calc(w)
            return (float(w))/1000 if self.isfloat(w) else np.nan
       elif w.endswith("l"):
            w=w.replace("l", " ")
            w=self.perform_calc(w)
       elif w.endswith("oz"):
            w=w.replace("oz", " ")
            w=self.perform_calc(w)
            return (float(w)) * 0.0283495 if self.isfloat(w) else np.nan
       else:
            np.nan

    def isfloat(self,w):
       try:
        float(w)
        return True
       except ValueError:
           return False
       
    def perform_calc(self, w):
        if 'x' in w:
            calc=w.split('x')
            return str(int(calc[0]) * int(calc[1]))
        return w
    
    def numeric(self, num):
        try:
            num.isnumeric()
            return True
        except:
            return False
        
    def isDigit(self, num):
        if str(num).isdigit() == True:
            return str(num)
        else:
            return np.nan
    
    



    
 