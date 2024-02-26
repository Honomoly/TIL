use('newDB')

// 전체 출력
db.product.find()


// 조건 출력
db.product.find({"prdNo":15})


// 원하는 부분만 출력
db.product.find({"prdNo":15}, {prdNo:1, prdName:1})


// show collections는 shell 명령문이라서 여기서는 못 씀
db.getCollectionNames()


// 컬렉션 생성
db.createCollection("book2")


// 여러개 추가하기 1
db.product.insertMany([ 
    {
        "prdNo": 19,
        "prdName": "알뜰 냉장고",
        "prdPrice": 1500000
    },
    {
        "prdNo": 20,
        "prdName": "고급 냉장고",
        "prdPrice": 3500000
    }
])


// 여러개 추가하기 2
prd1 = {
    "prdNo": 21,
    "prdName": "최고급 냉장고",
    "prdPrice": 5500000
}

prd2 = {
    "prdNo": 22,
    "prdName": "럭셔리 냉장고",
    "prdPrice": 7500000
}

db.product.insertMany([prd1, prd2])


// 수정하기
db.product.updateOne(
    {"prdNo": 22},
    {"$set":
        {"prdPrice": 8000000}
    }
)


// 여러 행 수정
db.book.updateMany(
    {"publisher.pubNo": "3"},
    {"$set":
        {"publisher.pubName": "정보출판사"}
    }
)


// upsert : true / 조건에 해당되는 도큐먼트가 없을 시 새로 추가
db.book.updateOne(
    {"bookAuthor": "이길동"},
    {$set:
        {
            "bookAuthorFirst": "길동",
            "bookAuthorSecond": "이"
        }
    },
    {upsert: true}
)


// 삭제하기 (사실 키는 따옴표 없어도 오류 없다)
db.book.deleteOne({bookAuthor: "이길동"})

