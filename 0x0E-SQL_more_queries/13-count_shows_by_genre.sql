-- script that lists all shows contained in hbtn_0d_tvshows without a genre linked.
SELECT tg.name as genre, COUNT(tg.name) as number_of_shows FROM tv_shows t LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id LEFT JOIN tv_genres tg ON tsg.genre_id = tg.id WHERE tg.name IS NOT NULL GROUP BY tsg.genre_id ORDER BY number_of_shows DESC;
