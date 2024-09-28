SELECT 
    ID,
    CASE
        WHEN size_of_colony <= 100 THEN 'LOW'
        WHEN size_of_colony <= 1000 then 'MEDIUM'
        ELSE 'HIGH'
    END AS SIZE
 
FROM ECOLI_DATA
ORDER BY ID ASC;