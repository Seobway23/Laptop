WITH ranked_data AS (
SELECT *,
    ROW_NUMBER() OVER(ORDER BY size_of_colony DESC) AS rn,
    COUNT(*) OVER() AS total
FROM ecoli_data
)

SELECT id,
    CASE 
        WHEN rn <= total*0.25 THEN "CRITICAL"
        WHEN rn > total*0.25 AND rn <= total*0.5 THEN "HIGH"
        WHEN rn > total*0.5 AND rn <= total*0.75 THEN "MEDIUM"
        ELSE "LOW"
    END AS colony_name
FROM ranked_data
ORDER BY id ASC;