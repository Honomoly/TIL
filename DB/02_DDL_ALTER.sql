-- 열 추가(동시 가능)
ALTER TABLE student ADD std_age INT;

-- 열 타입 변경
ALTER TABLE student MODIFY std_age INT;

-- 열 제약조건 변경
ALTER TABLE student MODIFY std_name VARCHAR(20) NOT NULL;

-- 열 이름 변경
ALTER TABLE student RENAME COLUMN std_tel TO std_phone;

-- 열 이름과 타입/제약조건 동시 변경
ALTER TABLE student CHANGE std_address std_address1 VARCHAR(50);

-- 열 삭제 
ALTER TABLE student DROP COLUMN std_address1;

DESCRIBE student;


-- 연습
ALTER TABLE product ADD (prdStock INT, prdDate DATE);
ALTER TABLE product MODIFY prdCompany VARCHAR(30) NOT NULL;
ALTER TABLE publisher ADD (pubPhone VARCHAR(13), pubAddress VARCHAR(50));
ALTER TABLE publisher DROP COLUMN pubPhone;

-- 기본키/외래키 삭제
ALTER TABLE student DROP PRIMARY KEY;
ALTER TABLE student DROP FOREIGN KEY FK_student_dptnum;

-- 기본키/외래키 추가
ALTER TABLE student ADD PRIMARY KEY (std_num);
ALTER TABLE student ADD CONSTRAINT FK_student_dptnum FOREIGN KEY (dpt_num) REFERENCES department (dpt_num);

-- 연습
-- 기본키 삭제를 위해서는 외래키 조건때문에 외래키 먼저 삭제가 필요
ALTER TABLE score DROP FOREIGN KEY FK_score_std;
ALTER TABLE score DROP FOREIGN KEY FK_score_course;
ALTER TABLE score DROP PRIMARY KEY;

ALTER TABLE score ADD CONSTRAINT FK_score_std FOREIGN KEY (std_num) REFERENCES student (std_num);
ALTER TABLE score ADD CONSTRAINT FK_score_course FOREIGN KEY (course_id) REFERENCES course (course_id);
ALTER TABLE score ADD PRIMARY KEY (std_num, course_id);


-- ON DELETE CASCADE : 참조된 테이블의 원본 데이터 삭제시 해당 데이터를 참조한 본 테이블의 데이터들 또한 자동으로 삭제
ALTER TABLE student DROP FOREIGN KEY FK_student_dptnum;
ALTER TABLE student
	ADD CONSTRAINT FK_student_dptnum
	FOREIGN KEY (dpt_num) REFERENCES department (dpt_num)
    ON DELETE CASCADE;


-- 테이블 삭제
DROP TABLE publisher;

-- 외래키 제약조건이 없으면 0, 있으면 1
SET FOREIGN_KEY_CHECKS = 0;