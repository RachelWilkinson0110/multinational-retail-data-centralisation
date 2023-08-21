SELECT 	COUNT (orders_table.product_quantity) AS sales_numbers,
	SUM(orders_table.product_quantity) AS product_quantity_count,
	CASE 
		WHEN dim_store_details.store_code = 'WEB-1388012W' then 'Web'
		ELSE 'In Store'
	END AS product_location
FROM orders_table
	JOIN dim_date_times ON  orders_table.date_uuid = dim_date_times.date_uuid
	JOIN dim_products ON  orders_table.product_code = dim_products.product_code
	JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY product_location
ORDER BY SUM(orders_table.product_quantity) ASC;