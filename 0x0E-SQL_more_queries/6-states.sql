-- Make the database 'hbtn_0d_usa'.
-- The script shouldn't fail if the database is already there.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- Construct the table "states" in the database "hbtn_0d_usa";
-- the primary key and id are both auto-generated, unique, and not null;
-- the name is VARCHAR(256), not null.
-- If the table is already there, the script shouldn't crash.
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states
(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256) NOT NULL,
	PRIMARY KEY (id)
);
