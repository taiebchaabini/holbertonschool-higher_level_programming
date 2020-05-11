-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT tg.name FROM tv_shows t LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id LEFT JOIN tv_genres tg ON tg.id = tsg.genre_id WHERE t.title = 'Dexter' ORDER BY tg.name ASC
