-- 뷰 생성
/*
기본 테이블보다 제한된 정보만 보이게 하는 역할을 주지만
보이는 내에서의 수정은 가능하다
*/
CREATE VIEW client_view
AS
SELECT clientNo, clientName, clientAddress
FROM client;

SELECT * FROM client_view;
INSERT INTO client_view VALUES('10', '케인', '제주');

-- 뷰에 추가
UPDATE client_view SET clientAddress='서울' WHERE clientNo='1';

-- 뷰에서 삭제
DELETE FROM client_view WHERE clientNo= '10';



-- 연습문제
CREATE VIEW top5_sales_clients
AS
SELECT C.clientNo 고객번호, clientName 고객명, SUM(bsQty) 총주문수량, SUM(bsQty*bookPrice) 총주문액
FROM client C
	INNER JOIN bookSale BS ON BS.clientNo = C.clientNo
	INNER JOIN book B ON B.bookNo = BS.bookNo
GROUP BY C.clientNo
ORDER BY SUM(bsQty*bookPrice) DESC
LIMIT 5;
DROP VIEW top5_sales_clients;


-- --------------------------------------------
-- 저장 프로시저
/*
마치 함수와 같이 과정을 저장해두었다가 호출하여 사용할 수 있다
출력하는 매커니즘이 길 경우 하나의 프로시저로 저장해서 그때그때 사용한다
*/
-- 정의
DROP PROCEDURE IF EXISTS clientProc;
DELIMITER $$
CREATE PROCEDURE clientProc()
BEGIN
	SELECT * FROM client;
END
$$ DELIMITER ;
-- 호출
CALL clientProc();

-- IN 매개변수
/*
다른 언어에서도 쉽게 찾아볼 수 있는 형태의 매개변수이다
*/
DROP PROCEDURE IF EXISTS clientProc2;
DELIMITER $$
CREATE PROCEDURE clientProc2(IN cName VARCHAR(20))
BEGIN
	SELECT * FROM client WHERE clientName = cName;
END
$$ DELIMITER ;

CALL clientProc2('메시');


-- 연습문제

DROP PROCEDURE IF EXISTS bookStockProc;
DELIMITER $$
CREATE PROCEDURE bookStockProc(IN inStock INT)
BEGIN
	SELECT bookNo 도서번호, bookName 도서명, bookAuthor 저자, bookPrice 가격,
		   (SELECT pubName
			FROM publisher
            WHERE publisher.pubNo = book.pubNo) 출판사
	FROM book
    WHERE bookStock > inStock;
END
$$ DELIMITER ;

CALL bookStockProc('5');

-- OUT 매개변수 / 출력 매개변수
/*
위와는 반대로 변수를 입력하면 그 변수가 프로시저를 거치면서
해당 변수에 원하는 값이 저장되는 형식이다
*/
DROP PROCEDURE IF EXISTS bookMaxProc;
DELIMITER $$
CREATE PROCEDURE bookMaxProc(OUT maxP INT)
BEGIN
	-- 도서 최고가를 maxP에 저장
	SELECT MAX(bookPrice) INTO maxP FROM book;
END
$$ DELIMITER ;

CALL bookMaxProc(@maxPrice);
SELECT @maxPrice;


-- 연습문제
DROP PROCEDURE IF EXISTS bookCountProc;
DELIMITER $$
CREATE PROCEDURE bookCountProc(OUT stocks INT)
BEGIN
	SELECT COUNT(*) INTO stocks
    FROM book
    WHERE bookPrice > 25000;
END
$$ DELIMITER ;

CALL bookCountProc(@nums);
SELECT @nums;


-- IN/OUT 둘 다 사용하기
DROP PROCEDURE IF EXISTS bookPriceCountProc;
DELIMITER $$
CREATE PROCEDURE bookPriceCountProc(IN inP INT, OUT outS INT)
BEGIN
	SELECT COUNT(*) INTO outS
    FROM book
    WHERE bookPrice > inP;
END
$$ DELIMITER ;

CALL bookPriceCountProc(20000, @books);
SELECT @books;


-- MySQL 변수선언으로 넣기
SET @price = 25000;
CALL bookPriceCountProc(@price, @books);
SELECT @books;


-- IF문
-- 해단 도서가 평균가 이상인지 아닌지 판단하기
DROP PROCEDURE IF EXISTS bookPriceCheckProc;
DELIMITER $$
CREATE PROCEDURE bookPriceCheckProc(IN bNo VARCHAR(20))
BEGIN
	-- 변수선언
	DECLARE bAVG INT;
    DECLARE bPrice INT;
    -- 변수저장
    SELECT AVG(bookPrice) INTO bAVG FROM book;
    SELECT bookPrice INTO bPrice FROM book WHERE bookNo = bNo;
    
    IF bPrice > bAVG THEN
		SELECT bAVG 평균, bPrice 도서가격, '평균가 이상' 결과;
	ELSE
		SELECT bAVG 평균, bPrice 도서가격, '평균가 이하' 결과;
	END IF;
END
$$ DELIMITER ;

CALL bookPriceCheckProc('1001');
CALL bookPriceCheckProc('1006');


-- 연습문제
DROP PROCEDURE IF EXISTS bookStockCheckProc;
DELIMITER $$
CREATE PROCEDURE bookStockCheckProc(IN bNo VARCHAR(20))
BEGIN
    DECLARE bStock INT;
    SELECT bookStock INTO bStock FROM book WHERE bookNo = bNo;
    
    IF bStock >= 7 THEN
		SELECT bStock 재고수량, '재고수준 보통' 결과;
	ELSE
		SELECT bStock 재고수량, '재고수준 위험' 결과;
	END IF;
END
$$ DELIMITER ;

CALL bookStockCheckProc('1001');
CALL bookStockCheckProc('1003');


-- CASE문
DROP PROCEDURE IF EXISTS clientAgeCheckProc;
DELIMITER $$
CREATE PROCEDURE clientAgeCheckProc(IN cNo INT)
BEGIN
	SELECT clientNo, clientName, clientBirth,
		CASE
			WHEN SUBSTR(clientBirth, 1, 3) = '197' THEN '1970년대생'
            WHEN SUBSTR(clientBirth, 1, 3) = '198' THEN '1980년대생'
            WHEN SUBSTR(clientBirth, 1, 3) = '199' THEN '1990년대생'
            ELSE '2000년대생'
		END 연령대
    FROM client
    WHERE clientNo = cNo;
END
$$ DELIMITER ;

CALL clientAgeCheckProc('1');


-- 연습문제
DROP PROCEDURE IF EXISTS clientRateCheckProc;
DELIMITER $$
CREATE PROCEDURE clientRateCheckProc(IN cNo INT)
BEGIN
	DECLARE cTotal INT;
    
    SELECT SUM(bsQty*bookPrice) INTO cTotal
    FROM bookSale
		INNER JOIN book ON book.bookNo = bookSale.bookNo
	WHERE clientNo = cNo;
        
	SELECT clientNo 고객번호, clientName 고객명, cTotal 총주문액,
		CASE
			WHEN cTotal >= 200000 THEN '최우수'
            WHEN cTotal >= 100000 THEN '우수'
            WHEN cTotal >= 50000 THEN '보통'
            ELSE '관심고객'
		END 고객등급
    FROM client
    WHERE clientNo = cNo;
END
$$ DELIMITER ;

CALL clientRateCheckProc('8');

-- 약간 변형
DROP PROCEDURE IF EXISTS clientRateCheckProc2;
DELIMITER $$
CREATE PROCEDURE clientRateCheckProc2()
BEGIN
	CREATE TABLE Total
    AS
    SELECT clientNo, SUM(bsQty*bookPrice) cTotal
    FROM bookSale
		INNER JOIN book ON book.bookNo = bookSale.bookNo
	GROUP BY clientNo;
        
	SELECT Total.clientNo 고객번호, clientName 고객명, cTotal 총주문액,
		CASE
			WHEN cTotal >= 200000 THEN '최우수'
            WHEN cTotal >= 100000 THEN '우수'
            WHEN cTotal >= 50000 THEN '보통'
            ELSE '관심고객'
		END 고객등급
    FROM Total
		INNER JOIN client ON client.clientNo = Total.clientNo;
    DROP TABLE Total;
END
$$ DELIMITER ;

CALL clientRateCheckProc2();





-- -------------------------------------------------
-- AUTO COMMIT 설정 확인 / 보통 디폴트로 설정되어 있움
SHOW VARIABLES LIKE 'autocommit';
-- 1이면 ON, 0이면 OFF이다
SET autocommit = 0;

-- ROLLBACK 확인
SELECT * FROM book;
UPDATE book SET bookAuthor='김길동' WHERE bookNo='1001';
ROLLBACK; -- 이게 있다고 무조건 취소되는건 아니다
SELECT * FROM book;

-- TRANSACTION 
/*
TRANSACTION 시작 후 ROLLBACK시 TRANSACTION을 했던 위치로 돌아온다!
체크포인트 설정의 개념이다
*/
START TRANSACTION;
SELECT * FROM book;
UPDATE book SET bookAuthor='김길동' WHERE bookNo='1001';
SELECT * FROM book;
ROLLBACK;
SELECT * FROM book;

-- COMMIT
/*
COMMIT 이후에는 ROLLBACK이 되지 않는다!
완전하게 저장이 된 것이다
*/
START TRANSACTION;
SELECT * FROM book;
UPDATE book SET bookAuthor='김길동' WHERE bookNo='1001';
SELECT * FROM book;
COMMIT;
ROLLBACK;
SELECT * FROM book;