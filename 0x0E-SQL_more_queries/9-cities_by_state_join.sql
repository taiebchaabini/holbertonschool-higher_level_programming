-- script that lists all cities contained in the database hbtn_0d_usa.
-- SELECT cities.id - cities.name - states.name 
SELECT c.id, c.name, s.name FROM cities c LEFT JOIN states s ON c.state_id = s.id
