ALTER TABLE orders_table
ALTER COLUMN card_number TYPE varchar USING card_number::varchar(9),
ALTER COLUMN store_code TYPE varchar USING store_code::varchar(11),
ALTER COLUMN product_code TYPE VARCHAR(255) USING product_code::varchar(9),
ALTER COLUMN product_quantity TYPE BIGINT USING product_quantity::BIGINT,
ALTER COLUMN user_uuid TYPE UUID USING user_uuid::UUID,
ALTER COLUMN date_uuid TYPE UUID USING date_uuid::UUID;