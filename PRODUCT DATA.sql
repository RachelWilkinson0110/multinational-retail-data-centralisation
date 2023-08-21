UPDATE dim_products
SET product_price= TRIM(LEADING '£' FROM product_price);

ALTER TABLE dim_products
ADD weight_class text;

ALTER TABLE dim_products
ALTER COLUMN product_price TYPE FLOAT USING product_price::FLOAT,
ALTER COLUMN weight TYPE FLOAT USING weight::FLOAT,
ALTER COLUMN product_code TYPE VARCHAR(11) USING product_code::varchar(11),
ALTER COLUMN weight_class TYPE VARCHAR(14) USING weight_class::varchar(14),
ALTER COLUMN date_added TYPE DATE USING date_added::date,
ALTER COLUMN uuid TYPE UUID USING uuid::UUID;

UPDATE dim_products
SET weight_class=
    (CASE 
         WHEN weight < 2 THEN 'Light'
         WHEN weight >= 2 and weight < 40 THEN 'Mid_sized'
	 	 WHEN weight >= 40 and weight < 140 THEN 'Heavy'
         else
             'Truck_Required'
     END); 
	 
ALTER TABLE dim_products
RENAME COLUMN removed to still_available;

ALTER TABLE "dim_products"
ALTER COLUMN "still_available"
SET DATA TYPE boolean
USING CASE
    WHEN "still_available" = 'Still_avaliable' then true
    WHEN "still_available" = 'Removed' then false
    ELSE null
END;

SELECT column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'public' AND 
table_name = 'dim_products';

ALTER TABLE dim_products
ADD PRIMARY KEY (product_code);

ALTER TABLE orders_table
ADD FOREIGN KEY (product_code) REFERENCES dim_products(product_code);
