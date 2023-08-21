SELECT  dim_date_times.year, 		  
    CONCAT('"hours": ',EXTRACT(hours FROM  avg(dim_date_times.time_diff)),' ',
		   '"minutes": ',EXTRACT(minutes FROM  avg(dim_date_times.time_diff)),' ',		  
		   '"seconds": ',round(EXTRACT(seconds FROM  avg(dim_date_times.time_diff)),2),' '		  
		  ) AS actual_time_taken		 		  
FROM dim_date_times
GROUP BY dim_date_times.year
ORDER BY AVG(dim_date_times.time_diff) DESC