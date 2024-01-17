-- create the MYSQL server user user_0d_1
-- user_0d_1 should have all the privilage on MYSQL server
-- user_0d_1 password should be set to user_0d_1_pwd
-- script should not fail if user_0d_1 exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
