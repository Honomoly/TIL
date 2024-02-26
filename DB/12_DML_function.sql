-- 내장함수
-- (1) ROUND()
-- ROUND(입력, 자릿수)

SELECT clientNo, ROUND(AVG(bookPrice*bsQty)) 평균주문액,
				 ROUND(AVG(bookPrice*bsQty), 1) 소수1자리,
                 ROUND(AVG(bookPrice*bsQty), 0) 없,
                 ROUND(AVG(bookPrice*bsQty), -1) 10의자리,
                 ROUND(AVG(bookPrice*bsQty), -2) 100의자리
FROM book, bookSale
WHERE book.bookNo = bookSale.bookNo
GROUP BY clientNo;

-- (2) format() / 위의 ROUND()와 동일 효과 / 천단위 구분도 해줌
SELECT clientNo, format(AVG(bookPrice*bsQty), 0) 소수0자리,
                 format(AVG(bookPrice*bsQty), 1) 소수1자리,
                 format(AVG(bookPrice*bsQty), 2) 소수2자리,
                 format(AVG(bookPrice*bsQty), 3) 소수3자리
FROM book, bookSale
WHERE book.bookNo = bookSale.bookNo
GROUP BY clientNo;

-- (3) RANK() / DENSE_RANK() / ROW_NUMBER()
SELECT bookPrice,
	   RANK() OVER (ORDER BY bookPrice DESC) 'RANK', -- 일반적인 순위표기 / 1, 1, 3, 4, ... 
       DENSE_RANK() OVER (ORDER BY bookPrice DESC) 'DENSE_RANK', -- 중도에 숫자가 끊킴없이 표기 / 1, 1, 2, 3, ...
       ROW_NUMBER() OVER (ORDER BY bookPrice DESC) 'ROW_NUMBER' -- 완전한 순위표기 / 1, 2, 3, 4, ...
FROM book;

-- (4) CHAR_LENGTH() : 글자수 / LENGTH() : 바이트수
/*
참고
UTF-8에서 한글은 글자당 3바이트의 용량을 가진다
영어및 특수문자는 1바이트다
*/
SELECT bookName 도서명,
	   CHAR_LENGTH(bookName) 글자수,
       LENGTH(bookName) 바이트수
FROM book
	INNER JOIN publisher
    ON book.pubNo = publisher.pubNo
WHERE pubName = '서울 출판사';

-- (5) SUBSTR() : 지정한 값만큼의 문자열만 출력
-- SUBSTR(입력, 시작, 길이)
SELECT DISTINCT bookAuthor 저자, SUBSTR(bookAuthor, 1, 1) 성, SUBSTR(bookAuthor, 2, 2) 이름
FROM book;


-- 연습문제
-- 1
SELECT DISTINCT bookAuthor 저자명, SUBSTR(bookAuthor, 1, 1) 성
FROM book
WHERE SUBSTR(bookAuthor, 1, 1) = '손';

-- 2
SELECT SUBSTR(bookAuthor, 1, 1) 성, COUNT(DISTINCT bookAuthor) 인원수
FROM book
GROUP BY SUBSTR(bookAuthor, 1, 1);


-- (6) 시간 관련 함수
SELECT DATE(NOW()) 날짜, TIME(NOW()) 시간;
SELECT YEAR(CURDATE()) 년, MONTH(CURDATE()) 월, DAYOFMONTH(CURDATE()) 일;
SELECT HOUR(CURTIME()) 시, MINUTE(CURTIME()) 분, SECOND(CURTIME()) 초, MICROSECOND(CURTIME()) 밀리초;
SELECT HOUR(CURRENT_TIME()) 시, MINUTE(CURRENT_TIME()) 분, SECOND(CURRENT_TIME()) 초, MICROSECOND(CURRENT_TIME()) 밀리초;

SELECT DATEDIFF('2025-01-01', NOW()), TIMEDIFF('23:23:59 ', CURTIME());


-- (7) LOAD_FILE() 함수
CREATE TABLE flower(
	flowerNo VARCHAR(10) NOT NULL PRIMARY KEY,
    flowerName VARCHAR(30),
    flowerInfo LONGTEXT,
    flowerImage LONGBLOB
);

INSERT INTO flower VALUES ('f003', '장미',
	LOAD_FILE('mass_files/rose.txt'),
    LOAD_FILE('mass_files/rose.jpg'));

-- 파일 업로드/다운로드 경로 변수 확인
SHOW variables LIKE 'secure_file_priv';


DROP TABLE flower;



-- ------------------------------------
-- 테이블 복사
CREATE TABLE new_book1 as
SELECT * FROM book;

-- 구조만 남기고 다 삭제
DELETE FROM new_book1;
SELECT * FROM new_book1;

-- 구조가 같으면 복사 가능
INSERT INTO new_book1 SELECT * FROM book;
SELECT * FROM new_book1;