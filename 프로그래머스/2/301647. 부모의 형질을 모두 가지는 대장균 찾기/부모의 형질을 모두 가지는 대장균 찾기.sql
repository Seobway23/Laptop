WITH parent_table AS (
SELECT id, parent_id, genotype AS parent_genotype
FROM ecoli_data)

# SELECT *
SELECT DISTINCT  A.id, A.genotype, parent_genotype
FROM ecoli_data A
JOIN parent_table B
ON A.parent_id = B.id
WHERE A.genotype & parent_genotype = parent_genotype
ORDER BY A.id ASC;