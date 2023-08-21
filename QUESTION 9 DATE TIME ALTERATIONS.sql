ALTER TABLE dim_date_times
ADD COLUMN time_diff interval;

UPDATE dim_date_times
SET time_diff = x.time_diff
FROM (
  SELECT timestamp, timestamp - LAG(timestamp) OVER (ORDER BY timestamp) AS time_diff
  FROM dim_date_times
) AS x
WHERE dim_date_times.timestamp = x.timestamp;