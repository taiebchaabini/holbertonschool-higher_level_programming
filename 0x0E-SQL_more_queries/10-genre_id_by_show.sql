-- script that lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
select t.title, tsg.genre_id FROM tv_shows t LEFT JOIN tv_show_genres tsg ON t.id = tsg.show_id WHERE tsg.genre_id IS NOT NULL ORDER BY t.title, tsg.genre_id ASC;
