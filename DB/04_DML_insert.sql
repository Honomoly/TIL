CREATE DATABASE sqldb2;
USE sqldb2;

CREATE TABLE publisher (
	pubNo VARCHAR(10) NOT NULL PRIMARY KEY,
    pubName VARCHAR(30) NOT NULL
);

CREATE TABLE book (
	bookNo VARCHAR(10) NOT NULL PRIMARY KEY,
    bookName VARCHAR(30) NOT NULL,
    bookPrice INT DEFAULT 10000 CHECK(bookPrice > 1000),
    bookDate DATE,
    pubNo VARCHAR(10) NOT NULL,
    CONSTRAINT FK_book_puublisher FOREIGN KEY (pubNo) REFERENCES publisher (pubNo)
);

-- INSERT INTO 테이블명 (테이블열명) VALUES (입력정보)
INSERT INTO publisher (pubNo, pubName) VALUES ('1', '서울출판사');
INSERT INTO publisher (pubNo, pubName) VALUES ('2', '강남출판사');
INSERT INTO publisher (pubNo, pubName) VALUES ('3', '종로출판사');

SELECT * FROM publisher; -- publisher의 각 열 내용 조회

INSERT INTO book (bookNo, bookName, bookPrice, bookDate, pubNo)
	VALUES ('1', '데이터베이스', 20000, '2022-11-11', '1');

INSERT INTO book -- 모든 열에 정보 입력시 입력하는 열 이름 생략 가능
	VALUES ('2', '파이썬', 23000, '2023-08-10', '2');

-- 한꺼번에 여러 정보 입력
INSERT INTO book (bookNo, bookName, bookPrice, bookDate, pubNo)
	VALUES 	('3', '알고리즘', 35000, '2023-08-01', '3'),
			('4', '자바스크립트', 22000, '2022-12-11', '2'),
			('5', 'HTML', 18000, '2023-04-23', '1');

-- 연습문제

CREATE TABLE department(
	dptNo VARCHAR(10) PRIMARY KEY,
    dptName VARCHAR(10) NOT NULL,
    dptTel VARCHAR(13)
);

CREATE TABLE student(
	stdNo VARCHAR(10) PRIMARY KEY,
	stdName VARCHAR(10) NOT NULL,
	stdYear INT DEFAULT 4 CHECK(stdYear>=1 AND stdYear<=4),
    stdAddress VARCHAR(50),
    stdBirthDay DATE NOT NULL,
    dptNo VARCHAR(10) NOT NULL,
    CONSTRAINT FK_student_department FOREIGN KEY (dptNo) REFERENCES department(dptNo)
);

INSERT INTO department
	VALUES	('1', '컴퓨터학과', '02-1111-1111'),
			('2', '경영학과', '02-2222-2222'),
            ('3', '수학과', '02-7777-7777');
INSERT INTO student
	VALUES	('2018002', '이몽룡', '4', '서울시 강남구', '1998-05-07', '1'),
			('2022003', '홍길동', '2', '경기도 안양시', '1999-11-11', '2'),
            ('2023003', '성춘향', '1', '전라북도 남원시', '2002-01-02', '3'),
            ('2021004', '변학도', '1', '서울시 종로구', '2000-11-11', '2');

SELECT * FROM department;
SELECT * FROM student;

CREATE TABLE board(
	boardNo INT AUTO_INCREMENT PRIMARY KEY, -- 자동 증가
    boardTitle VARCHAR(30) NOT NULL,
    boardWriter VARCHAR(20),
    boardContent VARCHAR(200),
    boardDate DATETIME DEFAULT CURRENT_TIMESTAMP -- 입력 없을 시 현재시각 입력
);

INSERT INTO board (boardTitle, boardWriter, boardContent)
	VALUES	('게시물 테스트', '익명1', '내용 입력하기'),
			('임의의 제목', '익명2', '내용은 없다');
    
SELECT * FROM board;


-- 외부에서 csv파일 import하기
-- 해당 DATABASE에서 우클릭하여 Table Data Import Wizard 실행
DESCRIBE product;
SELECT * FROM product;

ALTER TABLE product
	ADD PRIMARY KEY (prdNo),
	MODIFY	prdName VARCHAR(30),
	MODIFY	prdMaker VARCHAR(30),
	MODIFY	prdColor VARCHAR(20);

-- UPDATE문
UPDATE product SET prdName='UHD TV' WHERE prdNo='5';

-- DELETE문
DELETE FROM product WHERE prdName='그늘막 텐트';


-- 연습문제
INSERT INTO book
	VALUES	('9', 'JAVA 프로그래밍', '30000', '2022-03-10', '1'),
			('10', '파이썬 데이터 과학', '24000', '2023-09-05', '2');

UPDATE book SET bookPrice='25000' WHERE bookName='JAVA 프로그래밍';

DELETE FROM book WHERE bookDate >= '2022-01-01' AND bookDate < '2023-01-01';


-- 연습문제
CREATE TABLE customer(
	cusNo INT PRIMARY KEY,
    cusName VARCHAR(10),
    cusTel VARCHAR(13)
);

ALTER TABLE customer
	MODIFY cusTel VARCHAR(13) NOT NULL,
    ADD COLUMN cusGender VARCHAR(10),
    ADD COLUMN cusYear INT;

INSERT INTO customer
	VALUES	('1', '이몽룡', '010-1111-1111', '남자', '22'),
			('2', '성춘향', '010-2222-2222', '여자', '19'),
            ('3', '홍길동', '010-4444-4444', '남자', '30');

UPDATE customer SET cusTel='010-6666-6666' WHERE cusName='홍길동';

DELETE FROM customer WHERE cusYear < '20';