-- 코드를 작성해주세요
SELECT SUM(C.score) AS score, A.emp_no, A.emp_name, A.position, A.email
FROM HR_EMPLOYEES A
JOIN hr_grade C ON A.EMP_NO = C.EMP_NO
GROUP BY A.emp_no, A.emp_name, A.position, A.email
ORDER BY score DESC
LIMIT 1;