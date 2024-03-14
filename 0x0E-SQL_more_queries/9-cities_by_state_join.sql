-- States.name, cities.id, and cities.name should be shown for each record.
-- Limits one usage of the SELECT statement
SELECT cities.id, cities.name, states.name
FROM states
INNER JOIN cities
ON states.id = cities.state_id;
