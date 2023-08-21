ALTER TABLE dim_date_times
ALTER COLUMN month TYPE VARCHAR USING month::VARCHAR(2),
ALTER COLUMN day TYPE VARCHAR USING day::VARCHAR(2),
ALTER COLUMN year TYPE VARCHAR USING year::VARCHAR(4),
ALTER COLUMN time_period TYPE VARCHAR USING time_period::VARCHAR(10),
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND 
table_name = 'dim_date_times';

ALTER TABLE dim_date_times
ADD PRIMARY KEY (date_uuid);

ALTER TABLE orders_table
ADD FOREIGN KEY (date_uuid) REFERENCES dim_date_times(date_uuid);
