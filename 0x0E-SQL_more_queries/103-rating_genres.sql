-- script that lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
SELECT tg.name, SUM(tsr.rate) AS rating FROM tv_shows t
LEFT JOIN tv_show_ratings tsr ON tsr.show_id = t.id
LEFT JOIN tv_show_genres tsg ON tsg.show_id = t.id
LEFT JOIN tv_genres tg ON tg.id = tsg.genre_id
WHERE tg.name IS NOT NULL
GROUP BY tg.name ORDER BY rating DESC
