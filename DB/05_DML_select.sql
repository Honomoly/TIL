/*
SELECT 
		FROM
	   WHERE
	GROUP BY
	  HAVING
    ORDER BY
    
* : 모든 열 출력
DISTINCT : 중복되는 속성값이 있으면 한 번만 출력
*/

-- 데이터 설정

CREATE SCHEMA sqldb3;

USE sqldb3;

ALTER TABLE book
	MODIFY bookNo INT PRIMARY KEY,
    MODIFY bookName VARCHAR(20),
    MODIFY bookAuthor VARCHAR(10),
    MODIFY bookDate DATE;
    
ALTER TABLE bookSale
	MODIFY bsNo INT PRIMARY KEY,
    MODIFY bsDate DATE;
    
ALTER TABLE client
	MODIFY clientNo INT PRIMARY KEY,
    MODIFY clientName VARCHAR(10),
    MODIFY clientPhone VARCHAR(13),
    MODIFY clientAddress VARCHAR(20),
    MODIFY clientHobby VARCHAR(10),
    MODIFY clientGender VARCHAR(10),
	MODIFY clientBirth DATE;
    
ALTER TABLE publisher
	MODIFY pubNo INT PRIMARY KEY,
    MODIFY pubName VARCHAR(10);

ALTER TABLE book ADD
	CONSTRAINT FK_book_pubNo
	FOREIGN KEY (pubNo) REFERENCES publisher (pubNo);
    
ALTER TABLE bookSale ADD (
	CONSTRAINT FK_bs_clientNo
    FOREIGN KEY (clientNo) REFERENCES client (clientNo),
	CONSTRAINT FK_bs_bookNo
    FOREIGN KEY (bookNo) REFERENCES book (bookNo)
);


-- SELECT 사용
-- 전부 출력
SELECT * FROM book;

-- 도서명, 가격만 검색
SELECT bookName, bookPrice FROM book;

-- 저자만 검색(중복 제거)
SELECT DISTINCT bookAuthor FROM book;


-- WHERE 사용 (논리 연산자 사용)
-- 저자가 홍길동인 도서
SELECT bookName, bookAuthor FROM book
	WHERE bookAuthor='홍길동';

-- 가격이 3만원 이상의 도서
SELECT bookName, bookPrice, bookStock FROM book
	WHERE bookPrice >= '30000';

-- 재고가 3 ~ 5개인 도서
SELECT bookName, bookStock FROM book
	WHERE bookStock >= '3' AND bookStock <= '5';
    
SELECT bookName, bookStock FROM book
	WHERE bookStock BETWEEN 3 AND 5;
    
-- 출판사 번호가 1 또는 2 인 도서
SELECT bookName, pubNo FROM book
	WHERE pubNo='1' OR pubNo='2';

SELECT bookName, pubNo FROM book
	WHERE pubNo IN ('1', '2');
    
-- 출판사 번호가 1이 아닌 도서
SELECT bookName, pubNo FROM book
	WHERE NOT pubNo='1';
    
-- 취미에 null이 들어있는 행 검색
SELECT clientName, clientHobby FROM client
	WHERE clientHobby IS NULL; -- 비어있다고 null인건 아니다!
    
-- 빈칸의 일부를 null로 바꾼다
UPDATE client SET clientHobby=NULL
	WHERE clientName IN ('호날두', '샤라포바');
    
SELECT clientName, clientHobby FROM client
	WHERE clientHobby=''; -- 맥에선 스페이스 들어간건 공백으로 인식 안하네

-- 연습
SELECT bookName, bookAuthor, bookStock FROM book
	WHERE bookAuthor='홍길동' AND bookStock >= '3';

SELECT bookName, bookAuthor FROM book
	WHERE bookAuthor IN ('홍길동', '성춘향');
    
-- 패턴 매칭(LIKE)
/*
% : 0개 이상의 문자를 가진 문자열을 의미
_ : 단일문자를 의미(들어간 갯수만큼의 문자로 구성)
*/
-- 이름에 출판사가 포함된 출판사
SELECT * FROM publisher
	WHERE pubName LIKE '%출판사%';

-- 출생년도가 1990년대인 고객
SELECT * FROM client
	WHERE clientBirth LIKE '199%';
    
-- 이름이 4글자인 고객
SELECT * FROM client
	WHERE clientName LIKE '____';

-- 도서명에 안드로이드가 없는 도서
SELECT * FROM book
	WHERE NOT bookName LIKE '%안드로이드%';
SELECT * FROM book
	WHERE bookName NOT LIKE '%안드로이드%';
SELECT * FROM book
	WHERE !(bookName LIKE '%안드로이드%'); -- 다 된다!