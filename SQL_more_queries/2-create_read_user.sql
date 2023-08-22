-- To create the data base hbtn_0d_2.
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- Create the user user_0d_2.
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost';
-- The user_0d_2 password should be set to user_0d_2_pwd.
ALTER USER 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- Give select only privilege to user user_0d_2.
GRANT SELECT ON hbtn_od_2.* TO 'user_0d_2'@'localhost';
