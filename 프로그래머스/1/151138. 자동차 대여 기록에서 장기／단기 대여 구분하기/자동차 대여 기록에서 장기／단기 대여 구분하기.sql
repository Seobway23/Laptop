SELECT 
    history_id, 
    car_id,
    DATE_FORMAT(START_DATE, '%Y-%m-%d') AS start_date,
    DATE_FORMAT(END_DATE, '%Y-%m-%d') AS end_date,
    CASE
        WHEN DATEDIFF(END_DATE, START_DATE) + 1 >= 30 THEN '장기 대여'
        ELSE '단기 대여'
    END AS rent_type
FROM 
    CAR_RENTAL_COMPANY_RENTAL_HISTORY
WHERE 
    START_DATE BETWEEN '2022-09-01' AND '2022-09-30'
ORDER BY 
    history_id DESC;
