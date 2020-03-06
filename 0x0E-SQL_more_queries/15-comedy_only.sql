-- script that lists all Comedy shows in the database hbtn_0d_tvshows.
SELECT t.title FROM tv_shows t LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id LEFT JOIN tv_genres tg ON tg.id = tsg.genre_id WHERE tg.name = 'Comedy' ORDER BY t.title ASC
