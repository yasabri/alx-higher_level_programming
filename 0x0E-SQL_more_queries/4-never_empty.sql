-- Make the "id_not_null" table.
-- name VARCHAR(256) 
-- id INT default value 1 If the table is already there, the script shouldn't crash.
CREATE TABLE IF NOT EXISTS id_not_null (id INT DEFAULT 1, name VARCHAR(256));
