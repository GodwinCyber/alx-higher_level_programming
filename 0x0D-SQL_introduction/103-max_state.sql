-- import hbtn_0c_0 database this table dump
-- Display the maximum temp of each state (ordered by state name)
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state DESC LIMIT 3;
