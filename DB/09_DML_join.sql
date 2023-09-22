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

-- (5) INNER JOIN 명시법 / 가장 많이 사용되는 방법으로 권장된
SELECT C.clientNo, C.clientName, BS.bsDate, BS.bsQty
	FROM client C
		INNER JOIN bookSale BS
		ON C.clientNo = BS.clientNo;

-- ------------------------------------------------
SELECT * -- 두 테이블의 모든 정보가 출력
	FROM client C
		INNER JOIN bookSale BS
		ON C.clientNo = BS.clientNo;