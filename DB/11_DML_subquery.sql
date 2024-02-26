-- 고객명 호날두의 주문수량 조회
-- (1) 서브 쿼리 : clientName에서 clientNo을 찾는다
-- (2) 메인 쿼리 : 찾아온 clientNo로 bsQty을 찾는다


-- 단일행 서브쿼리 / 하나의 값으로 인식 / 대입 연산자 사용
SELECT bsDate, bsQty
FROM bookSale
WHERE clientNo = (SELECT clientNo
				  FROM client
                  WHERE clientName = '호날두');

SELECT SUM(bsQty)
FROM bookSale
WHERE clientNo = (SELECT clientNo
				  FROM client
                  WHERE clientName = '호날두');

SELECT bookName, bookPrice
FROM book
WHERE bookPrice = (SELECT MAX(bookPrice)
				   FROM book);
                   
SELECT bookName, bookPrice
FROM book
WHERE bookPrice > (SELECT AVG(bookPrice)
				   FROM book);
                   

-- 다중행 서브쿼리 / 여러 값으로 인식 / IN, NOT IN
SELECT clientNo, clientName
FROM client
WHERE clientNo IN (SELECT clientNo
				   FROM bookSale);

SELECT clientNo, clientName
FROM client
WHERE clientNo NOT IN (SELECT clientNo
					   FROM bookSale);

SELECT clientNo, clientName
FROM client
WHERE clientNo IN (SELECT clientNo
				   FROM bookSale
                   WHERE bookNo = (SELECT bookNo
								   FROM book
                                   WHERE bookName = '안드로이드 프로그래밍'));


SELECT clientNo, clientName
FROM client
WHERE clientNo IN (SELECT clientNo
				   FROM bookSale
                   WHERE bookNo IN (SELECT bookNo
								   FROM book
                                   WHERE bookName LIKE '%안드로이드%'));


-- EXISTS, NOT EXISTS
SELECT clientNo, clientName
FROM client
WHERE EXISTS (SELECT clientNo
			  FROM bookSale
              WHERE client.clientNo = bookSale.clientNo);

SELECT clientNo, clientName
FROM client
WHERE NOT EXISTS (SELECT clientNo
				  FROM bookSale
				  WHERE client.clientNo = bookSale.clientNo);


-- IN과 EXISTS의 차이
-- EXISTS는 존재하는지 아닌지만 확인 / NULL도 출력
SELECT clientNo, clientHobby
FROM client
WHERE EXISTS (SELECT clientHobby
			  FROM client);

-- 실제 값을 불러와서 비교를 한다 / NULL 출력하지 않음
SELECT clientNo, clientHobby
FROM client
WHERE clientHobby IN (SELECT clientHobby
			  FROM client);


-- ALL / 모든 것보다 커야함
SELECT clientNo, bsNo, bsQty
FROM bookSale
WHERE bsQty > ALL (SELECT bsQty
				   FROM bookSale
                   WHERE clientNo = '2');


-- ANY / 하나보다 크면 됨
SELECT clientNo, bsNo, bsQty
FROM bookSale
WHERE bsQty > ANY (SELECT bsQty
				   FROM bookSale
                   WHERE clientNo = '2');


-- 연습문제
-- 1. 고객 '호날두'가 주문한 도서의 총 구매량 출력 
SELECT SUM(bsQty) 총구매량
FROM bookSale
WHERE clientNo = (SELECT clientNo
				  FROM client
                  WHERE clientName = '호날두');
                  
-- 2. '정보출판사'에서 출간한 도서를 구매한 적이 있는 고객명 출력
SELECT clientName 고객명
FROM client
WHERE clientNo IN (SELECT clientNo
				   FROM bookSale
				   WHERE bookNo IN (SELECT bookNo
								    FROM book
                                    WHERE pubNo = (SELECT pubNo
												   FROM publisher
                                                   WHERE pubName = '정보출판사')));
                                                 
-- 3. 고객 '베컴'이 주문한 도서의 최고 주문수량보다 더 많은 도서를 구매한 고객명 출력
SELECT clientName 고객명
FROM client
WHERE clientNo IN (SELECT clientNo
				   FROM bookSale
                   WHERE bsQty > ALL (SELECT bsQty
									  FROM bookSale
                                      WHERE clientNo = (SELECT clientNo
													    FROM client
                                                        WHERE clientName = '베컴')));

-- 4. 서울에 거주하는 고객에게 판매한 도서의 총판매량 출력
SELECT SUM(bsQty) 총판매량
FROM bookSale
WHERE clientNo IN (SELECT clientNo
				   FROM client
                   WHERE clientAddress = '서울');



-- -------------------------------------------------
-- Scalar Subquery
/*
단일 반환값으로 나오는 형식을 말한다
일반적으로 SELECT나 UPDATE문과 함께 사용한다
*/
SELECT clientNo 고객번호, (SELECT clientName
						 FROM client
						 WHERE client.clientNo = bookSale.clientNo) 고객명, SUM(bsQty) 총주문량
FROM bookSale
GROUP BY clientNo;

-- 도서별로 판매대수를 표기하자면?
-- 도서테이블을 기준으로하면 모든 도서가 다 나온다 / 안팔린건 NULL로 표시된다
SELECT bookNo 도서번호, bookName 도서명, (SELECT SUM(bsQty)
									  FROM bookSale
                                      WHERE bookSale.bookNo = book.bookNo) 총주문수량
FROM book;
/*
WHERE (SELECT SUM(bsQty)
	   FROM bookSale
	   WHERE bookSale.bookNo = book.bookNo) IS NOT NULL;
뒤에 이런거 추가하기 싫으면 그냥 아래꺼 쓰자
*/

-- 도서판매테이블을 기준으로하면 판매된 도서에 대해서만 나온다
SELECT bookNo 도서번호, (SELECT bookName
					   FROM book
                       WHERE book.bookNo = bookSale.bookNo) 도서명, SUM(bsQty) 총주문수량
FROM bookSale
GROUP BY bookNo;


-- Inline View
/*
테이블 자체를 반환하는(다중 행) 형식이다
FROM절에 원하는 부분의 테이블만 도입하고 싶을때 사용한다
*/
-- 25000원 이상의 도서의 판매 정보
SELECT bookName 도서명, SUM(bookPrice) 도서가격, SUM(bsQty) 판매권수, SUM(bsQty*bookPrice) 총판매액
FROM (SELECT bookNo, bookName, bookPrice
	  FROM book
      WHERE bookPrice >= 25000)book_s, bookSale -- 인라인뷰 뒤에는 제목도 지정해주어야 한다(book_s)
WHERE book_s.bookNo = bookSale.bookNo
GROUP BY book_s.bookNo;

-- 거주지가 서울인 고객들이 25000원 이상의 도서를 구매한 정보
SELECT bookName 도서명, bookPrice 도서가격, SUM(bsQty) 총주문수량, SUM(bsQty*bookPrice) 총주문액
FROM (SELECT bookNo, bsQty
	  FROM bookSale
	  WHERE bookNo IN (SELECT bookNo
					   FROM book
					   WHERE bookPrice >= 25000
			AND
			clientNo IN (SELECT clientNo
						 FROM client
						 WHERE clientAddress = '서울'))) bookSale, book
WHERE bookSale.bookNo = book.bookNo
GROUP BY book.bookNo;
-- 또는
SELECT bookName 도서명, bookPrice 도서가격, SUM(bsQty) 총주문수량, SUM(bsQty*bookPrice) 총주문액
FROM (SELECT bookNo, bookName, bookPrice
	  FROM book
      WHERE bookPrice >= 25000) book,
	 (SELECT clientNo
      FROM client
      WHERE clientAddress = '서울') client,
      bookSale
WHERE book.bookNo = bookSale.bookNo AND bookSale.clientNo = client.clientNo
GROUP BY book.bookNo;