USE sqldb3;

-- JOIN 사용법
-- (1) WHERE 조건 사용
SELECT client.clientNo, clientName, bsDate, bsQty -- 어느 파일의 clientNo을 가져올지 모르기 때문에 지정해야 한다
	FROM client, bookSale -- 두 테이블을 가져옴
    WHERE client.clientNo = bookSale.clientNo; -- 각 테이블에 공통으로 들어간 열의 요소로 잇는다

-- (2) 모든 열 이름 앞에 테이블명을 붙이기도 한다
SELECT client.clientNo, client.clientName, bookSale.bsDate, bookSale.bsQty
	FROM client, bookSale
    WHERE client.clientNo = bookSale.clientNo;

-- (3) 별칭 사용법
SELECT C.clientNo, C.clientName, BS.bsDate, BS.bsQty
	FROM client C, bookSale BS -- 각 파일 줄여쓰
    WHERE C.clientNo = BS.clientNo;

-- (4) JOIN 명시법
SELECT C.clientNo, C.clientName, BS.bsDate, BS.bsQty
	FROM client C
		JOIN bookSale BS
		ON C.clientNo = BS.clientNo;

-- (5) INNER JOIN 명시법 / 가장 많이 사용되는 방법으로 권장됨
SELECT *
	FROM client C
		INNER JOIN bookSale BS
		ON C.clientNo = BS.clientNo;

-- ------------------------------------------------
-- 테이블 3개 결합 / JOIN 조건 2번 사용
SELECT BS.bsNo, C.clientName, B.bookName
	FROM bookSale BS
		INNER JOIN client C ON C.clientNo = BS.clientNo
        INNER JOIN book B ON B.bookNo = BS.bookNo;
        
SELECT BS.bsNo, BS.bsDate, C.clientNo, C.clientName, B.bookName, BS.bsQty
	FROM bookSale BS
		INNER JOIN client C ON C.clientNo = BS.clientNo
        INNER JOIN book B ON B.bookNo = BS.bookNo;

SELECT C.clientNo 고객번호, C.clientName 고객명, SUM(BS.bsQty) 총주문수량
	FROM bookSale BS
		INNER JOIN client C ON C.clientNo = BS.clientNo
        INNER JOIN book B ON B.bookNo = BS.bookNo
	GROUP BY C.clientNo
    ORDER BY 총주문수량 DESC;
    

SELECT BS.bsDate 주문일자, C.clientName 고객명, B.bookName 도서명, B.bookPrice 도서가격, BS.bsQty 주문수량, B.bookPrice*BS.bsQty 주문액
	FROM bookSale BS
		INNER JOIN client C ON C.clientNo = BS.clientNo
        INNER JOIN book B ON B.bookNo = BS.bookNo
    ORDER BY 주문일자;


SELECT BS.bsDate 주문일자, C.clientName 고객명, B.bookName 도서명, B.bookPrice 도서가격, BS.bsQty 주문수량, B.bookPrice*BS.bsQty 주문액
FROM bookSale BS
	INNER JOIN client C ON C.clientNo = BS.clientNo
	INNER JOIN book B ON B.bookNo = BS.bookNo
WHERE BS.bsDate >= '2021-01-01'
ORDER BY 주문일자;


-- --------------------------------------------------
-- 외부 조인 (OUTER JOIN) 
/*
두 테이블을 조인할 시 공통된 속성을 매개로 하는 정보가 한 테이블에 존재하지 않더라도
해당 정보를 버리지 않고 결과를 모두 표시한다
3가지의 형태가 있다
좌측 외부조인 / 우측 외부조인 / 완전 외부조인
*/

-- 왼쪽 외부조인
/*
왼쪽 테이블(client) 데이터 모두 출력하고 기준으로 오른쪽 테이블(bookSale)을 붙인다
이때 존재하지 않는 정보는 null로 채운다
*/
SELECT *
FROM client C
	LEFT OUTER JOIN bookSale BS
    ON C.clientNo = BS.clientNo
ORDER BY C.clientNo;

-- null을 이용해 한 번도 주문된 적 없는 책 찾기
SELECT B.bookNo, B.bookName
FROM book B
	LEFT OUTER JOIN bookSale BS
    ON BS.bookNo = B.bookNo
WHERE BS.bsNo IS NULL;


-- 오른쪽 외부조인
/*
위와는 반대다
오른쪽 테이블(bookSale) 데이터 모두 출력하고 기준으로 왼쪽 테이블(client)을 붙인다
이때 존재하지 않는 정보는 null로 채운다
*/
SELECT *
FROM client C
	RIGHT OUTER JOIN bookSale BS
    ON C.clientNo = BS.clientNo
ORDER BY C.clientNo;


-- 완전 외부조인
/*
MySQL에서는 완전 외부조인을 지원하지 않는다
그래서 오른쪽, 왼쪽 외부조인은 UNION해서 사용한다 
*/
SELECT *
FROM client C
	RIGHT OUTER JOIN bookSale BS
    ON C.clientNo = BS.clientNo

UNION -- 위 아래 두 테이블을 합치기

SELECT *
FROM client C
	LEFT OUTER JOIN bookSale BS
    ON C.clientNo = BS.clientNo
;