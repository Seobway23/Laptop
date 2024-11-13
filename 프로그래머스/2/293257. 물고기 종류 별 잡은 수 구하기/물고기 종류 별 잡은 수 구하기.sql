-- 코드를 작성해주세요
SELECT   COUNT(B.fish_name) AS fish_count, B.fish_name
FROM fish_info A
JOIN fish_name_info B
ON A.fish_type = B.fish_type
GROUP BY fish_name
ORDER BY fish_count DESC