// 1
use('test_db')
db.by_road_type.find({county: '강릉시'}, {"교차로내.accident_count":1})

// 2
use('test_db')
db.by_road_type.find({"기타단일로.death_toll": 0})

// 3
use('test_db')
db.by_type.find({
    type: "차대차",
    accident_count: {$gte: 100},
    death_toll: 0
})

// 4
use('test_db')
db.by_type.find({
    type: "차대차", $or: [
        {death_toll: 0},
        {heavy_injury: 0}
    ]
})

// 5
use('test_db')
db.area.find({county: /시$/})

// 6
use('test_db')
db.area.find({
    county: /군$/,
    population: {$gte: 100000}
})

// 7
use('test_db')
db.area.find({county: {
    $regex: /구$/,
    $gte: '아',
    $lt: '자'
}})

// 8
use('test_db')
db.by_month.find({
    city_or_province: "서울",
    "month_data.accident_count": {$gte: 200}
})

// 9
use('test_db')
db.by_month.find({$and: [
    {month_data: {$elemMatch: {"month": "01월", "heavy_injury": 0}}},
    {month_data: {$elemMatch: {"month": "02월", "death_toll": 0}}}
]})

// 10
use('test_db')
db.by_road_type.find({"기타단일로.death_toll": 0}, {city_or_province:1, county: 1, "기타단일로.death_toll": 1})

// 11 (콘솔창 출력)
use('test_db')
let lis = db.by_month.find({county: {$regex: /구$/, $gte: "아", $lt: "자"}})
lis.forEach(region => {
    console.log(region.city_or_province+" "+region.county)
    region.month_data.forEach(monthly => {
        if (monthly.accident_count >= 150) {
            console.log(monthly.month+" 사망자수 "+monthly.accident_count+"명")
        }
    })
    console.log("")
})

// 12 (콘솔창 출력)
use('test_db')
let lis2 = db.by_month.find({city_or_province: "서울", "month_data.accident_count": {$gte: 200}});
lis2.forEach(region => {
    console.log(region.county)
    let em = [];
    region.month_data.forEach(monthly => {
        if (monthly.accident_count >= 200) {
            em.push(monthly.month, monthly.accident_count)
        };
    });
    console.log(em[0]+" 사고횟수 "+em[1]+"회")
    console.log("")
})