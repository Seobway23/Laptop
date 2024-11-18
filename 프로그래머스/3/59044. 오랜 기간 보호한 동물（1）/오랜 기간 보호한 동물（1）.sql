SELECT A.name, A.datetime
FROM animal_ins A
LEFT JOIN animal_outs B
ON A.animal_id = B.animal_id
WHERE B.datetime IS NULL
ORDER BY A.DATETIME
LIMIT 3

# 입양을 못간 동물 중/ 
# 가장 오래 보호소에 있었던 동물 3마리 -> DATE -DESC
# SELECT 이름과 보호 시작일 조회
# 