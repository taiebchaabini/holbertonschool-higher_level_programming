-- script that lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_genres.name
SELECT t.title, tg.name FROM tv_shows t LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id LEFT JOIN tv_genres tg ON tg.id = tsg.genre_id ORDER BY t.title ASC, tg.name ASC
