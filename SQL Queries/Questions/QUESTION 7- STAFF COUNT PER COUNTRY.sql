SELECT  SUM(dim_store_details.staff_numbers) AS total_staff_numbers, 
	dim_store_details.country_code
FROM dim_store_details
GROUP BY dim_store_details.country_code