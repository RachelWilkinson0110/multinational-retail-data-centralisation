SELECT 	dim_store_details.store_type, 
		round(SUM (orders_table.product_quantity*dim_products.product_price)) AS revenue,
		round(SUM(100.0*orders_table.product_quantity*dim_products.product_price)/(SUM(SUM(orders_table.product_quantity*dim_products.product_price)) OVER ())) AS percentage_total
FROM orders_table
		JOIN dim_date_times ON  orders_table.date_uuid = dim_date_times.date_uuid
		JOIN dim_products ON  orders_table.product_code = dim_products.product_code
		JOIN dim_store_details ON orders_table.store_code = dim_store_details.store_code
GROUP BY dim_store_details.store_type
ORDER BY percentage_total DESC;