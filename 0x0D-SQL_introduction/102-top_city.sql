-- import hbtn_0c_0 database this table dump
-- Display the top 3 of cities during July and August
-- Ordered by temperature descending
SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month Between 7 AND 8 GROUP BY city ORDER BY avg_temp DESC LIMIT 3;
