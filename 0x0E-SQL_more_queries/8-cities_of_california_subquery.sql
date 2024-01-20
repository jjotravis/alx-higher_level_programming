-- Lists all cities of california in the DB hbtn_0d_usa
SELECT * FROM hbtn_0d_usa.cities
    WHERE state_id = (SELECT id FROM states WHERE name = 'California')
    ORDER BY id ASC;