15use('newDB')

// 연산자 쿼리

// 이상 / gte / Greater Then or Equal to
// 이하 / lte / Less Then or Equal to
db.product.find({prdPrice: {$gte: 2000000}}) // 2백만 이상
db.product.find({prdPrice: {$gte: 1000000, $lt: 2000000}}) // 백만 이상, 2백만 미만


// 논리 연산

// 또는 / or
db.product.find({$or:[
    {prdMaker:'삼성전자'},
    {prdMaker:'LG전자'}
]})

// 그리고 / and
db.product.find({$and:[
    {ctgNo: 2},
    {prdPrice: {$gte: 1000000}}
]})


// 문자열 연산자
// 문자 검색(띄어쓰기 기준) / $text, $search
// 먼저 해당 필드에 문자열 인덱스생성
db.book.createIndex({bookName: 'text', bookAuthor: 'text'}) // 두 필드에서 검색하게 됨
db.book.find({$text: {$search: '프로그래밍'}})


// 정규식
// '안'으로 시작하는 도서
db.book.find({bookName:/^안/})
// '밍'으로 끝나는 도서
db.book.find({bookName:/밍$/})
// 뒤에 .count()쓰면 갯수를 보여주는 메소드이다

// $regex : 여러 연산자 동시 사용을 가능하게 해주는 표현
// '밍'으로 끝나고 '안' ~ '자'까지 검색
db.book.find({bookName: {$regex: /밍$/, $gte: '안', $lt: '자'}})



// 배열 연산자 / Array
use('newDB')
db.createCollection("inventory")

db.inventory.insertMany(
    [
        {item: "journal", qty: 25, tags: ['blank', 'red']},
        {item: "notebook", qty: 50, tags: ['red', 'blank']},
        {item: "paper", qty: 100, tags: []},
        {item: "planner", qty: 75, tags: ['blank', 'red']},
        {item: "journal", qty: 45, tags: ['blue']}
    ]
)

use('newDB')
db.inventory.find({tags:'red'})

// 순서에 맞는 것만 출력
use('newDB')
db.inventory.find({tags:['red', 'blank']})

// 순서에 상관없이 출력
use('newDB')
db.inventory.find({tags: {$all: ['red', 'blank']}})


use('newDB')
db.createCollection('fruits')
db.fruits.insertMany([
    {_id: 1, fruit: ['apple', 'pear', 'banana']},
    {_id: 2, fruit: ['apple', 'banana', 'peach']},
    {_id: 3, fruit: ['cherry', 'pear', 'strawberry']},
    {_id: 4, fruit: ['rasberry', 'cherry', 'banana']}
])

use('newDB')
// 둘 다 포함되어야 함
db.fruits.find({fruit: {$all: ['apple', 'banana']}})

use('newDB')
// 하나만 있어도 됨
db.fruits.find({fruit: {$in: ['apple', 'banana']}})

use('newDB')
// 배열 요소가 3개인거
db.fruits.find({fruit: {$size: 3}})

use('newDB')
// 배열 요소가 4개인거는 없지만
db.fruits.find({fruit: {$size: 4}})

use('newDB')
// 배열 요소 추가하기
db.fruits.updateOne({_id: 4}, {$push: {fruit: "strawberry"}})



use('newDB')
db.createCollection("board")
db.board.insertOne({
    _id: 1,
    id: 1,
    comments: [
        {id: 1},
        {id: 2},
        {id: 3}
    ]
})
db.board.insertOne({
    _id: 2,
    id: 2,
    comments: [
        {id: 4},
        {id: 5},
        {id: 6}
    ]
})

use('newDB')
// comments에 id:5를 가지고 있는 것
db.board.find({"comments.id": 5})

use('newDB')
// 배열 안에서 인덱스를 지정하는 것도 가능하다 / 0번째 인덱스의 id:4인 것
db.board.find({"comments.0.id": 4})

use('newDB')
// 각 요소의 정보가 맞는 것 / 없으면 null이 나온다
db.board.findOne({comments: {$elemMatch: {id:5}}})

// 프로젝션 연산자 / $
// 'red'만 찾아서 태그의 'red'만 표시한다
use('newDB')
db.inventory.find({tags: 'red'}, {"tags.$":true})