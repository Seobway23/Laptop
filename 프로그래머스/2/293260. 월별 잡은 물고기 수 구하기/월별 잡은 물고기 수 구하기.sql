-- 코드를 작성해주세요
SELECT COUNT(*) as fish_count, MONTH(time) as month
FROM fish_info
GROUP BY MONTH(time)
ORDER BY MONTH(time)