-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- SELECT c.id and c.name from states where the cities state id is equal to states id
SELECT c.id, c.name FROM cities c LEFT JOIN states s ON c.state_id = s.id WHERE c.state_id = 1;
