$(document).ready(function(){
    $('#prdSearchForm2').on('submit', function(){
        // 새로고침 막기
        event.preventDefault();

        // 폼에 입력한 값을 쿼리 스트링으로 변환
        // serialize() 메소드 사용
        // ex) type=prd_name&keyword=자전거
        let form_data = $(this).serialize();

        $.ajax({ // 데이터 통신
            type: 'post', // 보내는 데이터 형식
            url: '/product_search2/', // 데이터를 보낼 주소
            data: form_data, // 보내는 데이터
            datatype: 'json', // 보내는 데이터 타입
            success: function(result){ // 위의 요청이 성공하면 result로 받을 데이터를 가져온더
                console.log(result); // 테스트 출력
                // 성공시 가져온 result를 가지고 수행할 명령
                const prd_list = result.prd_list_json
                $('#searchResultBox2').empty();

                // jQuery로 테이블 생성하기
                const str = `
                    <table id="result_prd_list2" class="table_format">
                        <tr>
                            <th>상품번호</th>
                            <th>상품명</th>
                            <th>가격</th>
                            <th>제조회사</th>
                            <th>색상</th>
                            <th>카테고리번호</th>
                        </tr>
                `
                $('#searchResultBox2').append(str);

                // 데이터 길이가 0이면(검색 결과 없음) 따로 처리
                if (prd_list.length == 0) {
                    $('#result_prd_list2').append('<tr align="center"><td colspan="5">찾는 상품이 없습니다</td></tr>')
                } else {
                    for (i=0; i<prd_list.length; i++) {
                        $('#result_prd_list2').append('<tr><td>' +
                            prd_list[i].pk + '</td><td>' +
                            prd_list[i].fields.prd_name + '</td><td>' +
                            prd_list[i].fields.prd_price + '</td><td>' +
                            prd_list[i].fields.prd_maker + '</td><td>' +
                            prd_list[i].fields.prd_color + '</td><td>' +
                            prd_list[i].fields.ctg_no + '</td></tr>'
                        )
                    };
                    $('#result_prd_list2').append('</table>')
                }
            },
            error: function(){
                // 오류 발생하면 실행할 명령
                alert('오류 발생')
            },
            complete: function(){

            }
        });
    });
});