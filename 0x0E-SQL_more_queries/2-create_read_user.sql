-- script that creates the database hbtn_0d_2 and the user user_0d_2.
CREATE DATABASE hbtn_0d_2 IF NO EXISTS;
-- CREATE USER user_0d_2
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- GRANT SELECT PRIVILEGES
GRANT SELECT PRIVILEGES ON *.* TO user_0d_2@localhost;
