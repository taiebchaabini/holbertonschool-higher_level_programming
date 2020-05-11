-- script that lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
SELECT t.title, tsg.genre_id FROM tv_shows t LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id ORDER BY t.title, tsg.genre_id ASC;
