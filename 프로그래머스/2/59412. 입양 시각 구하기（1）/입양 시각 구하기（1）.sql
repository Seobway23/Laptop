SELECT HOUR(datetime) AS hour, count(*) AS count
FROM animal_outs
WHERE HOUR(datetime) >= 9 AND HOUR(datetime) <= 19
GROUP BY HOUR(datetime)
ORDER BY HOUR(datetime)