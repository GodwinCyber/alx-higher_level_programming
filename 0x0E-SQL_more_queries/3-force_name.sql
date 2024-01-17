-- creates the table force_name on your MySQL server.
-- force_name description
-- id INT
-- name VARCHAR(256) cant't be NULL
-- database name will be passed as an argument of the mysql command
-- script should not fail if force_name exist
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
