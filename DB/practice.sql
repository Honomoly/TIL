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