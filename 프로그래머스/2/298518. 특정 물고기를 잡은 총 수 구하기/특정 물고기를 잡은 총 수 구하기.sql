SELECT count(*) AS fish_count
FROM fish_info A
JOIN FISH_NAME_INFO B
ON A.fish_type = B.fish_type
WHERE B.fish_name = 'BASS' OR B.fish_name = 'SNAPPER'