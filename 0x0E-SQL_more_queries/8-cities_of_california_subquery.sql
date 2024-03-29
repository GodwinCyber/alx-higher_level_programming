-- show all the cities of California that can be found in the database hbtn_0d_usa
-- The states table contains only one record where name = California (but the id can be different, as per the example)
-- database name will be passed as an argument of the mysql command
-- You are not allowed to use the JOIN keyword
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California');
