-- import hbtn_0c_0 database this table dump
-- Display the average temperature (Fahrenheit)
-- By citye oredered by temperature (descending)
SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY avg_temp DESC;
