-- lists every entry in my MySQL server's second_table that has a name value.
-- Records are arranged in decreasing score order.
SELECT `score`, `name`
FROM `second_table`
WHERE `name` != ""
ORDER BY `score` DESC
