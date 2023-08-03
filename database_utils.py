import pandas as pd
from sqlalchemy import create_engine

class DatabaseConnector:
    
    def __init__(self):
        pass

    def upload_to_db(self, pd_df, table_name):
        conn_string='postgresql://postgres:Nellie3101@localhost/sales_data'
        db=create_engine(conn_string)
        df=pd_df
        df.to_sql(table_name, db, if_exists="replace")
        

    


