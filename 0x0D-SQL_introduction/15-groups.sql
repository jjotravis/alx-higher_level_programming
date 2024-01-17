-- script that list number of records with same value
-- query to list number of same records in second_table
SELECT score, COUNT(*) AS number
FROM second_table
GROUP BY score ORDER BY score DESC;
