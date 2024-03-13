-- displays the quantity of records in my MySQL server's second_table that have the same score.
-- Records are ordered by descending count.
SELECT `score`, COUNT(*) AS `number`
FROM `second_table`
GROUP BY `score`
ORDER BY `number` DESC;
