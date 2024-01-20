-- Lists all cities contained in the DB hbtn_0d_usa
SELECT c.id, c.name, s.name
FROM  cities as c
    INNER JOIN states as s
    ON c.state_id = s.id;