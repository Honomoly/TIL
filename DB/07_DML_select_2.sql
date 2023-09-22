USE sqldb3;

-- ORDER BY 사용
/*
특정 열을 기준으로 결과값 정렬
ASC : 오름차순 (생략시 디폴드값)
DESC : 내림차순
*/

-- 오름차순
SELECT * FROM book
	ORDER BY bookName ASC;
    
-- 내림차순
SELECT * FROM book
	ORDER BY bookName DESC;
    
-- 참고 : 내림차순으로 한글이 먼저 나오기 위해서는 ASCII 코드를 조정해야 한다
SELECT * FROM book
	ORDER BY (CASE
		WHEN ASCII(SUBSTRING(bookName, 1)) BETWEEN 48 AND 57 THEN 3
		WHEN ASCII(SUBSTRING(bookName, 1)) < 122 THEN 2
        ELSE 1 END),
        bookName DESC;

-- 상위 N개만 출력 : LIMIT N
SELECT * FROM book
	ORDER BY bookName ASC
	LIMIT 5;
    
-- 6에서 시작하여 5개
SELECT * FROM book
	ORDER BY bookName ASC
	LIMIT 5 OFFSET 6;

-- 재고수량 기준 정렬
SELECT bookName, bookAuthor, bookStock FROM book
	ORDER BY bookStock DESC;
    
-- 2차 정렬
-- 재고수량이 동일하면 저자명으로 정렬
SELECT bookName, bookAuthor, bookStock FROM book
	ORDER BY bookStock DESC, bookAuthor;


-- ------------------------------------
-- 집계함수
/*
SUM()
AVG()
MAX()
MIN()
COUNT() / * 입력시 전체 행 갯수 출력
*/

-- SUM()
SELECT SUM(bookStock) FROM book;
SELECT SUM(bookStock) AS '총 재고량' FROM book; -- 이름 지정 / 띄어쓰기를 안 쓰면 따옴표 없어도 됨 / AS 생략 가능

SELECT SUM(bsQty) AS '호날두의 주문수량' FROM bookSale
	WHERE clientNo='2';

-- MAX(), MIN()
SELECT MAX(bsQty) AS '최대 주문량', MIN(bsQty) AS '최소 주문량' FROM bookSale;

-- All functions
SELECT	SUM(bookPrice*bookStock) '가격 총액',
		ROUND(AVG(bookPrice)) '평균 가격', -- ROUND(수, 소수이하 자리수) 
		MAX(bookPrice) '최고가',
        MIN(bookPrice) '최저가'
        FROM book;

-- COUNT()
SELECT COUNT(*) AS '총 판매건수', SUM(bsQty) AS '총 판매수량' FROM bookSale;

-- null값은 세지 않는다
SELECT COUNT(clientHobby) '취미' FROM client; -- null을 제외한 7개
SELECT COUNT(clientHobby) '취미' FROM client 
	WHERE NOT clientHobby=''; -- null과 공백을 제외한 5개

-- 중복하여 세지 않는 법
SELECT COUNT(DISTINCT bookAuthor) '저자' FROM book;



-- GROUP BY 사용
/*
기준이 되는 열에서 같은 원소끼리 취합한다
*/
SELECT bookNo, SUM(bsQty) AS '주문수량 합계'
	FROM bookSale
    GROUP BY bookNo; -- bookNo가 일치하는 것들 끼리 모아 출력
    
-- ORDER BY 다음에 정렬하려는 이름에 따옴표가 있으면 정렬이 안된다
SELECT bookNo, SUM(bsQty) AS 주문수량합계
	FROM bookSale
    GROUP BY bookNo
    ORDER BY 주문수량합계;
    
-- 정렬하려는 기준열을 지정해주면 가능
SELECT bookNo, SUM(bsQty) AS '주문수량 합계'
	FROM bookSale
    GROUP BY bookNo
    ORDER BY 2;


-- --------------------------------------------
-- HAVING 사용
/*
GROUP BY에 의해 구성된 그룹들에 대해 적용할 조건을 지정한다
주의점!
1. 반드시 GROUP BY와 함께 사용한다
2. WHERE의 뒤에 온다
3. 검색조건에 집계함수가 포함되어야 한다
*/

SELECT pubNo, COUNT(*) '도서 종류 갯수'
	FROM book
	WHERE bookPrice >= 20000 -- 갸격이 20000원 이상인 책들만 사용
    GROUP BY pubNo -- 출판사 별로 그룹화 
    HAVING COUNT(*) >= 2 -- 각 출판사에서 출판한 책 종류가 2가지 이상
    ORDER BY 2; -- 도서 종류 갯수 기준으로 정렬