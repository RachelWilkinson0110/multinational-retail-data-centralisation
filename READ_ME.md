<h1>  Retail Data Centralisation <h1>

<h4> In this project we create a local PostgreSQL database to which we upload data from different sources. Once we have uploaded the data to our database we then create a database schema and run SQL queries on the data.

<h2> Project code <h2>

<h4> There are 4 documents containing the code used for this project:

1. data_extraction.py <br>
As the name suggests this code focuses on extracting the relevant data from each of the different data sources (discussed below).

2. data_cleaning.py<br>
Once we had successfully extracted the data the next step was to clean the data of any invalid data (duplicates, null etc).

3. database_utilis.py<br>
This file contains the code used to establish a connection with our PostgreSQL database and the upload of the data we have extracted and cleaned.

4. main.py<br>
This file contains 6 different functions for the extraction, cleaning and upload of the data. The files mentioned in 1, 2 and 3 are imported and then called within the different functions.

<h2> Data Sources <h2>

<h4>We extract data from various sources in this project:

1. Remote postgres database in AWS Cloud<br>
We retrieve both the orders data and user data from this source. The order data is uploaded to our PostgreSQL datbase as **orders_table**. this table will become the fact table in our starbased schema. The user data is uploaded to the database as **dim_users** and this is the first of five dimension tables in our schema. The primary key in this table is **user_uuid**.

2. Link in AWS Cloud
We extracted the card details data via a link. The card data was stored in a pdf so we used read_pdf from the tabula package to extract the data. The card data was uploaded to our database as **dim_card_details** with the primary key being **card_number**.


3. AWS S3 Bucket<BR>
The product details were stored in an AWS S3 bucket. We used the botos3 package to extract this data. The product details were uploaded to our database as **dim_products** with the primary key being **product_code**.


4. Restful-API<br>
Details on each store was extracted via and API using the GET method. These details were uploaded as **dim_store_details** and the primary key is **store_code**.


5. Link
Date and time data was accessed via a link and extracted. This data was then uploaded to the PostgreSQL database as **dim_date_times**. This is the final dimension table in our star based schema. The primary key for this table is **date_uuid**.

<h2> SQL <h2>

<h4> Before carrying out any queries on the data we first needed to perform some alterations:

* Ensure that each column in every table had the correct data type.
* Assign the primary keys
* Assign the foreign keys

The SQL was similar for each of the tables - I have added an example below. The SQL for altering each of the tables can be found in the folder 'SQL queries'. 

*Correcting data type for dim_users table*
![Alt text](Screenshot%202023-08-16%20at%2014.52.22.png)

*Adding the primary and foreign keys for the dim_users table*

![Alt text](Screenshot%202023-08-16%20at%2014.52.32.png)

Once the data alterations have been made we then ran queries to answer business questions - the SQL for this can be found in 'SQL Queries'.