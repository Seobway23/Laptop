SELECT DISTINCT D.id,	D.email,	D.first_name,	D.last_name
FROM developers D, skillcodes S
WHERE (D.skill_code & S.code) = S.code
AND (S.name = 'Python' OR S.name = 'C#')
ORDER BY D.id ASC;