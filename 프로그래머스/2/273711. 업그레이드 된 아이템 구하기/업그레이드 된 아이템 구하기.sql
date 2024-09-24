WITH upgrade AS (
SELECT A.item_id
FROM item_tree A
JOIN item_info B
ON B.item_id = A.item_id
WHERE B.RARITY = 'RARE'
)

SELECT A.item_id, item_name, rarity
FROM ITEM_TREE A
JOIN ITEM_INFO B
ON B.ITEM_ID = A.ITEM_ID
WHERE A.PARENT_ITEM_ID IN (SELECT item_id FROM upgrade)
ORDER BY ITEM_ID DESC