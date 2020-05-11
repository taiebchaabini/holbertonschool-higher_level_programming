-- script that lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
SELECT t.title, SUM(tsr.rate) AS rating FROM tv_shows t LEFT JOIN tv_show_ratings tsr ON t.id = tsr.show_id GROUP BY t.title ORDER BY rating DESC;
