-- List all cities of CA that can be found in db 'hbtn_0d_usa'
-- 'states' table contains only one record where 'name = California
-- Results must sorted in ascending order by 'cities.id'
-- do not  allowed to use JOIN keyword
SELECT id, name
FROM cities
WHERE state_id = (
      SELECT id
      FROM states
      WHERE name = 'California'
);
