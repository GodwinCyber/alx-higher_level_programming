Read or watch:

What is Database & SQL?
A Basic MySQL Tutorial
Basic SQL statements: DDL and DML (no need to read the chapter “Privileges”)
Basic queries: SQL and RA
SQL technique: functions
SQL technique: subqueries
What makes the big difference between a backtick and an apostrophe?
MySQL Cheat Sheet
MySQL 8.0 SQL Statement Syntax
installing MySQL in Ubuntu 20.04
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What’s a database
What’s a relational database
What does SQL stand for
What’s MySQL
How to create a database in MySQL
What does DDL and DML stand for
How to CREATE or ALTER a table
How to SELECT data from a table
How to INSERT, UPDATE or DELETE data
What are subqueries
How to use MySQL functions
Copyright - Plagiarism
You are tasked to come up with solutions for the tasks below yourself to meet with the above learning objectives.
You will not be able to meet the objectives of this or any following project by copying and pasting someone else’s work.
You are not allowed to publish any content of this project.
Any form of plagiarism is strictly forbidden and will result in removal from the program.
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25)
All your files should end with a new line
All your SQL queries should have a comment just before (i.e. syntax above)
All your files should start by a comment describing the task
All SQL keywords should be in uppercase (SELECT, WHERE…)
A README.md file, at the root of the folder of the project, is mandatory
The length of your files will be tested using wc
More Info
Comments for your SQL file:
$ cat my_script.sql
-- 3 first students in the Batch ID=3
-- because Batch 3 is the best!
SELECT id, name FROM students WHERE batch_id = 3 ORDER BY created_at DESC LIMIT 3;
$
Install MySQL 8.0 on Ubuntu 20.04 LTS
$ sudo apt update
$ sudo apt install mysql-server
...
$ mysql --version
mysql  Ver 8.0.25-0ubuntu0.20.04.1 for Linux on x86_64 ((Ubuntu))
$
Connect to your MySQL server:

$ sudo mysql
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 11
Server version: 8.0.25-0ubuntu0.20.04.1 (Ubuntu)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
mysql> quit
Bye
$
Use “container-on-demand” to run MySQL
In the container, credentials are root/root

Ask for container Ubuntu 20.04
Connect via SSH
OR connect via the Web terminal
In the container, you should start MySQL before playing with it:
$ service mysql start                                                   
 * Starting MySQL database server mysqld 
$
$ cat 0-list_databases.sql | mysql -uroot -
Database                                                                                   
information_schema                                                                         
mysql                                                                                      
performance_schema                                                                         
sys                      
$

SQL - Introduction
What’s a database: DataBase is the arrangement of data in orderly manner that it can be accessed through a medium
What’s a relational database:
A relational database is a specific type of database that provides a structured mechanism for organising and accessing data. It uses a predefined format with tables, and examples of such databases include MySQL and MsSQL, where data is stored in a tabular form.
What does SQL stand for: Structured Query Language 
What’s MySQL: MySQL, which stands for "Structured Query Language," is a relational database management system (DBMS). It is widely used for organising and managing data in a structured format. MySQL stores data in tables, allowing for efficient and organised storage, retrieval, and manipulation of information through SQL queries.
How to create a database in MySQL
What DDL and DML stand for: DDL stands for Data Definition language while DML stands for Data manipulation Language. DDL is used to build and modify the structure of your table and other objects in the database. DDL takes effect immediately while DML is a statement used to work with data in the table. 
How to CREATE or ALTER a table: Creating or Altering a table is called DDL. Your first type CREATE TABLE <specify the attribute name > <data type>. Example below 
	CREATE TABLE <table name> ( 
        <attribute name 1> <data type 1>,
        …
        <attribute name n> <data type n>). This also applied to ALTERING a table. ALTER TABLE <table name>
       ADD CONSTRAINT <constraint name> PRIMARY KEY (<attribute list>);
How to SELECT data from a table: Select is DML and is also part of retrieving data from an already existing table, it is working data in an already existing table. Example       
SELECT {attribute}+
  FROM {table}+
  [ WHERE {boolean predicate to pick rows} ]
  [ ORDER BY {attribute}+ ];
How to INSERT, UPDATE or DELETE data: These are all DML statement and there examples:
UPDATE <table name>
SET <attribute> = <expression>
WHERE <condition>
DELETE FROM <table name>
WHERE <condition>;
INSERT INTO <table name>
VALUES (<value 1>, ... <value n>)
What are subqueries: Subqueries is method of querying sql to provide information using assumed data from possible data of your locations, name (first_name, last_name), zip_code, etc. Examples 
SELECT cFirstName, cLastName, cZipCode
FROM customers
WHERE cZipCode =        
      (SELECT cZipCode
FROM customers
       WHERE cFirstName = 'Wayne' AND cLastName = 'Dick');
Here the information of Wayne Dick is used to get Alvaro Mongo
