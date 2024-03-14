-- Create user 'user_0d_1'
-- Password for user as 'user_0d_1_pwd'
-- The script shouldn't fail if the user is already there.
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.*
TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
