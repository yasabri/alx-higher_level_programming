-- Create table 'force_name'
-- Name VARCHAR(256), id INT, must be null
-- If the table is already there, the script shouldn't crash.
CREATE TABLE IF NOT EXISTS force_name (id INT, name VARCHAR(256) NOT NULL);
