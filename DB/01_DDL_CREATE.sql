-- 스키마 생성
CREATE SCHEMA sqldb1 DEFAULT CHARACTER SET 'utf8';
CREATE SCHEMA sqldb2 DEFAULT CHARACTER SET 'utf8mb4';

-- 스키마 삭제
DROP SCHEMA sqldb1;
DROP SCHEMA sqldb2;

--
CREATE SCHEMA sqldb1 DEFAULT CHARACTER SET 'utf8mb4';



-- 테이블 생성
CREATE TABLE product(
	prdNo VARCHAR(10) NOT NULL PRIMARY KEY,
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    prdCompany VARCHAR(30)
);

CREATE TABLE product2(
	prdNo VARCHAR(10) NOT NULL PRIMARY KEY,
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    prdCompany VARCHAR(30)
);
-- 제약조건 따로 걸기
CREATE TABLE product3(
	prdNo VARCHAR(10) NOT NULL,
    prdName VARCHAR(30) NOT NULL,
    prdPrice INT,
    prdCompany VARCHAR(30),
    CONSTRAINT PK_product_prdNo PRIMARY KEY (prdNo)
    /*
		CONSTRAINT [제약조건명] : 제약조건에 이름을 붙여 나중에 삭제/추가를 용이하게 만든다
        PRIMARY KEY ([컬럼명]) : 주어진 컬럼에 기본키 설정을 할당
	*/
);

-- 기본키/외래키 제약조건 설정
/*
출판사 테이블 생성
pubNo가 기본키
pubName은 NOT NULL
*/
CREATE TABLE publisher(
	pubNo VARCHAR(10) NOT NULL PRIMARY KEY,
    pubName VARCHAR(30) NOT NULL
);
/*
도서 테이블 생성 (도서번호, 도서명, 가격, 발행일, 출판사번호)
bookNo가 기본키
pubNo가 외래키로 들어감
*/
CREATE TABLE book(
	bookNo VARCHAR(10) NOT NULL PRIMARY KEY,
    bookName VARCHAR(30) NOT NULL,
    bookPrice INT DEFAULT 10000 CHECK(bookPrice > 1000),
    bookDate DATE,
    pubNo VARCHAR(10) NOT NULL,
    FOREIGN KEY (pubNo) REFERENCES publisher (pubNo)
    -- FOREIGN KEY (현재 테이블 열 이름)  REFERENCES 참조 테이블 (참조 테이블의 기본키)
);

DESCRIBE book;

-- 연습1
CREATE TABLE department(
    dep VARCHAR(30) NOT NULL PRIMARY KEY
);

CREATE TABLE student(
	 student_name VARCHAR(20) NOT NULL PRIMARY KEY,
     dep VARCHAR(30) NOT NULL,
     student_year INT CHECK(student_year >= 1 AND student_year <= 4),
     FOREIGN KEY (dep) REFERENCES department (dep)
);

-- 연습2
CREATE TABLE department(
	dept_num INT NOT NULL PRIMARY KEY,
	dept_name VARCHAR(30) NOT NULL
);

CREATE TABLE employee(
	emp_name VARCHAR(20) NOT NULL PRIMARY KEY,
    emp_year INT,
    dept_num INT NOT NULL,
    FOREIGN KEY (dept_num) REFERENCES department (dept_num)
);

-- 연습4
CREATE TABLE department(
	dpt_num INT NOT NULL PRIMARY KEY,
    dpt_name VARCHAR(30),
    dpt_tel VARCHAR(20)
);

CREATE TABLE student(
	std_num INT NOT NULL PRIMARY KEY,
    std_name VARCHAR(30) NOT NULL,
    std_year INT CHECK(std_year >= 1 AND std_year <= 4),
    std_tel VARCHAR(20),
    std_address VARCHAR(40),
    dpt_num INT,
    FOREIGN KEY (dpt_num) REFERENCES department (dpt_num)
);

CREATE TABLE professor(
	prof_id VARCHAR(20) NOT NULL PRIMARY KEY,
    prof_name VARCHAR(20),
    prof_tel VARCHAR(20),
    dpt_num INT,
    FOREIGN KEY (dpt_num) REFERENCES department (dpt_num)
);

CREATE TABLE course(
	course_id VARCHAR(20) NOT NULL PRIMARY KEY,
    course_title VARCHAR(40),
    course_credit INT,
    prof_id VARCHAR(20),
    FOREIGN KEY (prof_id) REFERENCES professor (prof_id)
);

CREATE TABLE score(
	std_num INT,
    course_id VARCHAR(20),
	CONSTRAINT FK_score_std FOREIGN KEY (std_num) REFERENCES student (std_num),
    CONSTRAINT FK_score_course FOREIGN KEY (course_id) REFERENCES course (course_id),
    CONSTRAINT PK_num_id PRIMARY KEY (std_num, course_id) -- 복합키 설정
);


-- 자동증가
CREATE TABLE board(
	boardNo INT AUTO_INCREMENT NOT NULL PRIMARY KEY,
    boardName VARCHAR(30)
);
