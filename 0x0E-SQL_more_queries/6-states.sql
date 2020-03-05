-- script that creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa) on your MySQL server.
-- CREATE DATABASE hbtn_0d_usa if NOT EXISTS
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- CREATE TABLE IF NO EXISTS named STATES
CREATE TABLE IF NO EXISTS states(
	id INT UNIQUE NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(256) NOT NULL
);
