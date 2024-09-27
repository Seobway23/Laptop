WITH ecoli_table AS (
    SELECT id
    FROM ECOLI_DATA  
)
, ecoli_child AS (
    SELECT parent_id AS id, COUNT(*) AS child_count
    FROM ECOLI_DATA 
    GROUP BY parent_id
    HAVING parent_id IS NOT NULL
)

SELECT A.id, IFNULL(B.child_count, 0)  AS CHILD_COUNT
FROM ecoli_table A
LEFT JOIN ecoli_child B
ON A.id = B.id

# SELECT A.id, B.parent_id
# FROM ecoli_table A
# JOIN ecoli_cild_table B
# WHERE A.id = B.id