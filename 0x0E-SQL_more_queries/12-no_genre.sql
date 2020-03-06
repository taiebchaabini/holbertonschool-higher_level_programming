-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT t.title, tsg.genre_id FROM tv_shows t LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id WHERE tsg.genre_id IS NULL ORDER BY t.title, tsg.genre_id ASC;
