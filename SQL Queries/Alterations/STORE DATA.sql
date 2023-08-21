ALTER TABLE dim_store_details
ALTER COLUMN longitude TYPE float USING longitude::float,
ALTER COLUMN locality TYPE varchar USING locality::varchar(255),
ALTER COLUMN store_code TYPE VARCHAR USING store_code::varchar(10),
ALTER COLUMN staff_numbers TYPE smallint USING staff_numbers::smallint,
ALTER COLUMN opening_date TYPE date USING opening_date::date,
ALTER COLUMN store_type TYPE varchar USING store_type::varchar(255),
ALTER COLUMN latitude TYPE float USING latitude::float,
ALTER COLUMN country_code TYPE varchar USING country_code::varchar(2),
ALTER COLUMN continent TYPE varchar USING continent::varchar(255);
