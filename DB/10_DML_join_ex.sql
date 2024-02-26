-- 1. 모든 도서에 대하여 도서의 도서번호, 도서명, 출판사명 출력
SELECT B.bookNo 도서번호, B.bookName 도서명, P.pubName 출판사명
FROM book B INNER JOIN publisher P ON P.pubNo = B.pubNo;

-- 2. '서울 출판사'에서 출간한 도서의 도서명, 저자명, 출판사명 출력 (조건에 출판사명 사용)
SELECT B.bookName 도서명, B.bookAuthor 저자명, P.pubName 출판사명
FROM book B INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName= '서울 출판사';

-- 3. '정보출판사'에서 출간한 도서 중 판매된 도서의 도서명 출력 (중복된 경우 한 번만 출력) (조건에 출판사명 사용)
SELECT DISTINCT B.bookName 도서명
FROM book B
	INNER JOIN publisher P ON P.pubNo = B.pubNo
    INNER JOIN bookSale BS ON BS.bookNo = B.bookNo
WHERE P.pubName= '정보출판사';

-- 4. 도서가격이 30,000원 이상인 도서를 주문한 고객의 고객명, 도서명, 도서가격, 주문수량 출력
SELECT C.clientName 고객명, B.bookName 도서명, B.bookPrice 도서가격, BS.bsQty 주문수량
FROM bookSale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
    INNER JOIN book B ON B.bookNo = BS.bookNo
WHERE B.bookPrice >= 30000;

-- 5. '안드로이드 프로그래밍' 도서를 구매한 고객에 대하여 도서명, 고객명, 성별, 주소 출력 (고객명으로 오름차순 정렬)
SELECT B.bookName 도서명, C.clientName 고객명, C.clientGender 성별, C.clientAddress 주소
FROM bookSale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
    INNER JOIN book B ON B.bookNo = BS.bookNo
WHERE B.bookName = '안드로이드 프로그래밍'
ORDER BY 고객명;

-- 6. ‘도서출판 강남'에서 출간된 도서 중 판매된 도서에 대하여 ‘총 매출액’ 출력
SELECT SUM(BS.bsQty*B.bookPrice) 총매출액
FROM bookSale BS
	INNER JOIN book B ON B.bookNo = BS.bookNo
    INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName = '도서출판 강남';

-- 7. ‘서울 출판사'에서 출간된 도서에 대하여 판매일, 출판사명, 도서명, 도서가격, 주문수량, 주문액 출력
SELECT BS.bsDate 판매일, P.pubName 출판사명, B.bookName 도서명, B.bookPrice 도서가격, BS.bsQty 주문수량, B.bookPrice*BS.bsQty 주문액
FROM bookSale BS
    INNER JOIN book B ON B.bookNo = BS.bookNo
    INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName = '서울 출판사'
ORDER BY 판매일;

-- 8. 판매된 도서에 대하여 도서별로 도서번호, 도서명, 총 주문 수량 출력
SELECT B.bookNo 도서번호, B.bookName 도서명, SUM(BS.bsQty) 총주문수량
FROM bookSale BS
    INNER JOIN book B ON B.bookNo = BS.bookNo
GROUP BY B.bookNo;

-- 9. 판매된 도서에 대하여 고객별로 고객명, 총구매액 출력 ( 총구매액이 100,000원 이상인 경우만 해당)
SELECT C.clientName 고객명, SUM(B.bookPrice*BS.bsQty) 총구매액
FROM bookSale BS
	INNER JOIN book B On B.bookNo = BS.bookNo
    INNER JOIN client C ON C.clientNo = BS.clientNo
GROUP BY C.clientNo
HAVING SUM(B.bookPrice*BS.bsQty) >= 100000;

-- 10. 판매된 도서 중 ＇도서출판 강남'에서 출간한 도서에 대하여 고객명, 주문일, 도서명, 주문수량, 출판사명 출력 (고객명으로 오름차순 정렬)
SELECT C.clientName 고객명, BS.bsDate 주문일, B.bookName 도서명, BS.bsQty 주문수량, P.pubName 출판사명
FROM bookSale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
	INNER JOIN book B ON B.bookNo = BS.bookNo
    INNER JOIN publisher P ON P.pubNo = B.pubNo
WHERE P.pubName = '도서출판 강남'
ORDER BY 고객명;