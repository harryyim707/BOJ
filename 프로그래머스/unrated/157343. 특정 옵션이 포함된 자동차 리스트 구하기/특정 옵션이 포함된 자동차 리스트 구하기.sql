-- 코드를 입력하세요
SELECT *
FROM CAR_RENTAL_COMPANY_CAR C
WHERE C.OPTIONS LIKE '%네비게이션%'
ORDER BY C.CAR_ID DESC
;