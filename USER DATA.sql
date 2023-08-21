ALTER TABLE dim_users
ALTER COLUMN first_name TYPE varchar USING first_name::varchar(255),
ALTER COLUMN last_name TYPE varchar USING last_name::varchar(255),
ALTER COLUMN country_code TYPE VARCHAR(2) USING country_code::varchar(2),
ALTER COLUMN date_of_birth TYPE date USING date_of_birth::date,
ALTER COLUMN join_date TYPE date USING join_date::date,
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND 
table_name = 'dim_users';

ALTER TABLE dim_users
ADD PRIMARY KEY (user_uuid);

DELETE FROM orders_table
WHERE user_uuid IN(
	SELECT  DISTINCT user_uuid 
	FROM orders_table 
	WHERE user_uuid 
	NOT IN (SELECT user_uuid FROM dim_users));

ALTER TABLE orders_table
ADD FOREIGN KEY (user_uuid) REFERENCES dim_users(user_uuid);



