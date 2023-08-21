ALTER TABLE dim_card_details
ALTER COLUMN card_number TYPE varchar USING card_number::varchar(9),
ALTER COLUMN expiry_date TYPE varchar USING expiry_date::varchar(5),
ALTER COLUMN date_payment_confirmed TYPE date USING date_payment_confirmed::date;

ALTER TABLE dim_card_details
ADD PRIMARY KEY (card_number);

DELETE FROM orders_table
WHERE card_number IN(
	SELECT  DISTINCT card_number 
	FROM orders_table 
	WHERE card_number 
	NOT IN (SELECT card_number FROM dim_card_details));

ALTER TABLE orders_table
ADD FOREIGN KEY (card_number) REFERENCES dim_card_details(card_number);