-- script that uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT DISTINCT tg.name FROM tv_genres tg 
WHERE NOT EXISTS(SELECT tsg.genre_id FROM tv_shows t
LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id
WHERE t.title = "Dexter" AND tg.id = tsg.genre_id)
ORDER BY tg.name ASC
