-- script that lists all records of a table
-- query to list all records of the table second_table with names
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
