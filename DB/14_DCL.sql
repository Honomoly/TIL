USE sqldb3;
USE mysql;

SELECT * FROM user;

-- 계정생성
CREATE USER newuser1@'%' IDENTIFIED BY '1111';
/*
여기서 connection을 만들어도 아무 권한이 없기 때문에 접속이 안된다
*/

-- 비밀번호 변경
SET PASSWORD FOR 'newuser1'@'%' = '1234';

-- 계정 삭제
DROP USER 'newuser1'@'%';


-- -------------------------------------------------
CREATE USER newuser1@'%' IDENTIFIED BY '1111';
-- 권한 조회
SHOW GRANTS FOR newuser1;

-- 모든 권한 부여
GRANT ALL PRIVILEGES ON *.* TO 'newuser1'@'%';

-- SELECT 권한 제거
REVOKE SELECT ON *.* FROM 'newuser1'@'%';

-- SELECT 권한 다시 부여
GRANT SELECT ON *.* TO 'newuser1'@'%';