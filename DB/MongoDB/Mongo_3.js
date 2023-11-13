// find()에서 컬렉션 내 도큐멘트 출력
use('newDB')
db.book.find().count()

// 그렇다고 Array의 요소를 다 활용할 수 있는 것은 아니다
use('newDB')
db.book.find().length // 오류!(undefined)

// 서로 다른 저자 출력하기
use('newDB')
db.book.distinct("bookAuthor")

// 근데 얘는 또 왜 킹받게 Array냐
use('newDB')
db.book.distinct("bookAuthor").length // 오류 안남!

// 이건 요소가 도큐먼트 아니라고 count()을 못 쓴다
use('newDB')
db.book.distinct("bookAuthor").count() // 오류!


// 출판사별로 그룹지어서 총재고수량 계산하기
use('newDB')
db.book.aggregate([
    {'$group': { // 대괄호(배열 표현)을 먼저 쓰는 것이 특징
        _id: {'출판사': '$publisher.pubName'}, // 그룹화 할 필드 지정
        '총재고수량': {$sum: '$bookStock'} // 그룹내 계산하는 값
    }}
])

// 평균 버전
use('newDB')
db.book.aggregate([
    {'$group': {
        _id: {'출판사': '$publisher.pubName'},
        '평균재고수량': {$avg: '$bookStock'}
    }}
])

// 정렬하기
use('newDB')
db.book.aggregate([
    {'$group': {
        _id: {'출판사': '$publisher.pubName'},
        '총재고수량': {$sum: '$bookStock'}
    }},
    {'$sort': {'총재고수량': 1}} // 오름차순 / -1이면 내림차순
])

// 출판사별 최고가, 최저가
use('newDB')
db.book.aggregate([
    {'$group': {
        _id: {'출판사': '$publisher.pubName'},
        '최고가': {$max: '$bookPrice'},
        '최저가': {$min: '$bookPrice'},
    }}
])

// 그룹화할 필드 지정을 하지 않으면 전체에서 찾는다
use('newDB')
db.book.aggregate([
    {'$group': {
        _id : {},
        '최고가': {$max: '$bookPrice'},
        '최저가': {$min: '$bookPrice'},
    }}
])

// 도시별 인구수
use('test_db')
db.area.aggregate([
    {'$group': {
        _id : {'도시' : '$city_or_province'},
        '인구수': {$sum: '$population'},
    }},
    {'$sort': {'인구수': -1}}
])

// 도시별 인구수 Top5
use('test_db')
db.area.aggregate([
    {'$group': {
        _id : {'도시' : '$city_or_province'},
        '인구수': {$sum: '$population'},
    }},
    {'$sort': {'인구수': -1}},
    {'$limit': 5}
])

// 도시별 인구수 Bottom5
use('test_db')
db.area.aggregate([
    {'$group': {
        _id : {'도시' : '$city_or_province'},
        '인구수': {$sum: '$population'},
    }},
    {'$sort': {'인구수': 1}},
    {'$limit': 5}
])

// 도시별 인구수 / $match가 뒤에 오면 안되네...?
use('test_db')
db.area.aggregate([
    {'$match': {'city_or_province': '서울'}},
    {'$group': {
        _id : {'도시' : '$city_or_province'},
        '인구수': {$sum: '$population'},
    }},
])

// 도시별 인구수 3백만 이상
use('test_db')
db.area.aggregate([
    {'$group': {
        _id : {'도시' : '$city_or_province'},
        '인구수': {$sum: '$population'},
    }},
    {'$sort': {'인구수': -1}},
    {'$match': {'인구수': {$gte: 3000000}}}
])

// 서울 구 수
use('test_db')
db.area.aggregate([
    {'$match': {'city_or_province': '서울'}},
    {'$group': {
        _id : {'도시' : '$city_or_province'},
        '구 수': {$sum: 1}
    }}
])

// 50만 이상의 자치구 수
use('test_db')
db.area.aggregate([
    {'$match': {'population': {$gte: 500000}}},
    {'$group': {
        _id : {
            '도시': '$city_or_province',
            '자치구': '$county'
        },
        '인구수' : {$sum: '$population'}
    }}
])


use('test_db')
db.local.aggregate([
    {'$match': {'sub_category': '의회비'}},
    {'$group': {
        _id : {
            '도시': '$city_or_province',
        },
        '의회비' : {$sum: '$this_term_expence'}
    }}
])