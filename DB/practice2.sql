CREATE SCHEMA modeling_db;
USE modeling_db;

CREATE TABLE member (
	memID VARCHAR(45) PRIMARY KEY
);

CREATE TABLE category (
	ctgNo INT PRIMARY KEY,
    ctgName VARCHAR(30)
);

CREATE TABLE product (
	prdNo INT PRIMARY KEY,
    prdName VARCHAR(60),
    ctgNo INT
);

CREATE TABLE cart (
    memID VARCHAR(45),
    prdNo INT,
    Quantity INT
);

CREATE TABLE order_info (
	ordNo INT,
	prdNo INT,
	Quantity INT
);

CREATE TABLE order_product (
	ordNo INT PRIMARY KEY,
    memID VARCHAR(45),
    ordName VARCHAR(21),
    ordPhone VARCHAR(13),
    ordAddress VARCHAR(60)
);

ALTER TABLE product
	ADD CONSTRAINT FK_product_ctgNo
    FOREIGN KEY (ctgNo) REFERENCES category (ctgNo);

ALTER TABLE cart 
	ADD CONSTRAINT FK_cart_memID
    FOREIGN KEY (memID) REFERENCES member (memID),
	ADD CONSTRAINT FK_cart_prdNo
    FOREIGN KEY (prdNo) REFERENCES product (prdNo);
    
ALTER TABLE cart
	ADD CONSTRAINT PK_cart
    PRIMARY KEY (memID, prdNo);

ALTER TABLE order_info
	ADD CONSTRAINT FK_order_info_ordNo
    FOREIGN KEY (ordNo) REFERENCES order_product (ordNo),
    ADD CONSTRAINT FK_order_info_prdNo
    FOREIGN KEY (prdNo) REFERENCES product (prdNo);

ALTER TABLE order_info
	ADD CONSTRAINT PK_order_info
    PRIMARY KEY (ordNo, prdNo);

ALTER TABLE order_product
	ADD CONSTRAINT FK_order_product_memID
    FOREIGN KEY (memID) REFERENCES member (memID);