-- script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT t.title FROM tv_shows t
WHERE NOT EXISTS(SELECT tg.name FROM tv_genres tg
LEFT JOIN tv_show_genres tsg ON tsg.genre_id = tg.id
WHERE tg.name = 'Comedy' and tsg.show_id = t.id)
ORDER BY t.title ASC
