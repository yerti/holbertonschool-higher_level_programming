-- Create the user user_0d_1
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost';
-- Give user privileges user_0d_1 
GRANT ALL PRIVILEGES ON * . * TO 'user_0d_1'@'localhost';
-- The user_0d_1 password should be set to user_0d_1_pwd 
ALTER USER 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1pwd';
