-- script that creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa) on your MySQL server.
-- CREATE DATABASE hbtn_0d_usa IF NOT EXISTS
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
-- CREATE THE TABLE CITIES IF NO EXISTS
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256) NOT NULL,
	FOREIGN KEY (state_id) REFERENCES states(id)
);