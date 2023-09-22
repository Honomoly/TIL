-- (1) 도서 테이블에서 가격 순으로 내림차순 정렬하여,  도서명, 저자, 가격 출력 (가격이 같으면 저자 순으로 오름차순 정렬)
SELECT bookName, bookAuthor, bookPrice
	FROM book
	ORDER BY bookPrice DESC, bookAuthor;
    
-- (2) 도서 테이블에서 저자에 '길동'이 들어가는 도서의 총 재고 수량 계산하여 출력v
SELECT SUM(bookStock) '길동 관련 책 수량'
	FROM book
    WHERE bookAuthor LIKE '%길동%';
    
-- (3) 도서 테이블에서 ‘서울 출판사' 도서 중 최고가와 최저가 출력 
SELECT MAX(bookPrice) '최고가', MIN(bookPrice) '최저가'
	FROM book
    WHERE pubNo='1';

-- (4) 도서 테이블에서 출판사별로 총 재고수량과 평균 재고 수량 계산하여 출력 (‘총 재고 수량’으로 내림차순 정렬)
SELECT 	pubNo '출판사 번호',
		ROUND(SUM(bookStock), 1) '총 재고수량',
		ROUND(AVG(bookStock), 1) '책별 평균수량'
	FROM book
    GROUP BY pubNo
    ORDER BY 2 DESC;

-- (5) 도서판매 테이블에서 고객별로 ‘총 주문 수량’과 ‘총 주문 건수’ 출력. 단 주문 건수가 2이상인 고객만 해당
SELECT 	clientNo '고객번호',
		SUM(bsQty) '총 주문수량',
		COUNT(*) '총 주문건수'
	FROM bookSale
    GROUP BY clientNo
    HAVING COUNT(*) >= 2
    ORDER BY 3 DESC;