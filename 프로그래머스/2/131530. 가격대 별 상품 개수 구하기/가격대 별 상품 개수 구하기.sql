SELECT TRUNCATE(PRICE / 10000, 0) * 10000 AS price_group, COUNT(*) AS products
FROM PRODUCT
GROUP BY TRUNCATE(PRICE / 10000, 0)
ORDER BY ROUND(PRICE / 10000, 0) * 10000  ASC
