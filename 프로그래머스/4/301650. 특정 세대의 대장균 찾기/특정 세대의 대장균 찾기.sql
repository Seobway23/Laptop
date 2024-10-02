WITH selected_table AS (
    SELECT 
        child.ID AS child_id, 
        child.PARENT_ID AS parent_id, 
        parent.ID AS "부모", 
        grandparent.ID AS P_Parent,
        great_grandparent.ID AS P_P_Parent
FROM 
    ECOLI_DATA child
LEFT JOIN 
    ECOLI_DATA parent ON child.PARENT_ID = parent.ID
LEFT JOIN 
    ECOLI_DATA grandparent ON parent.PARENT_ID = grandparent.ID
LEFT JOIN 
    ECOLI_DATA great_grandparent ON grandparent.PARENT_ID = great_grandparent.ID
HAVING P_Parent IS NOT NULL AND P_P_Parent IS NULL                      
)

SELECT child_id AS ID
FROM selected_table
ORDER BY child_id
                        