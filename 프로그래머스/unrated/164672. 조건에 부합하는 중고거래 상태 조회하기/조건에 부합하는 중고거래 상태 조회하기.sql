-- 코드를 입력하세요
SELECT B.BOARD_ID, B.WRITER_ID, B.TITLE, B.PRICE,
(CASE WHEN B.STATUS = 'SALE' THEN '판매중'
WHEN B.STATUS = 'RESERVED' THEN '예약중'
WHEN B.STATUS = 'DONE' THEN '거래완료'
END
) AS 'STATUS'
FROM USED_GOODS_BOARD B
WHERE DATE_FORMAT(B.CREATED_DATE, '%Y-%m-%d') = DATE_FORMAT('2022-10-05','%Y-%m-%d')
ORDER BY B.BOARD_ID DESC;