SELECT  ROUTE, 
        CONCAT(ROUND(SUM(D_BETWEEN_DIST), 1), 'km') AS TOTAL_DISTANCE,
        CONCAT(ROUND(AVG(D_BETWEEN_DIST), 2), 'km') AS AVERAGE_DISTANCE
FROM subway_distance
GROUP BY ROUTE
# concat을 쓰면 제대로 order 되지 않으므로, row data에 직접 접근한다 
ORDER BY SUM(D_BETWEEN_DIST) DESC