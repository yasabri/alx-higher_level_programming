-- Make the "unique_id" table.
-- name VARCHAR(256), id INT default 1 unique
-- If the table is already there, the script shouldn't crash.
CREATE TABLE IF NOT EXISTS unique_id
(
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256)
);
