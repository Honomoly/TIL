$(document).ready(function(){
    $('#book_search').on('submit', function(){
        event.preventDefault();

        const form_data = $(this).serialize();

        $.ajax({
            type: 'post',
            url: '/book/search/',
            data: form_data,
            datatype: 'json',
            success: function(result){
                const prd_list = result.book_list_json
                $('#searched_result').empty();
                const str = `
                    <table id="searched_result_table" class="book_list">
                        <tr>
                            <th>도서번호</th>
                            <th>도서명</th>
                            <th>저자</th>
                            <th>가격</th>
                            <th>출판일자</th>
                            <th>재고수량</th>
                            <th>출판사</th>
                        </tr>
                `
                $('#searched_result').append(str);

                // 데이터 길이가 0이면(검색 결과 없음) 따로 처리
                if (prd_list.length == 0) {
                    $('#searched_result_table').append('<tr align="center"><td colspan="5">찾는 상품이 없습니다</td></tr>')
                } else {
                    for (i=0; i<prd_list.length; i++) {
                        $('#searched_result_table').append('<tr><td>' +
                            prd_list[i].pk + '</td><td>' +
                            prd_list[i].fields.book_name + '</td><td>' +
                            prd_list[i].fields.book_author + '</td><td>' +
                            prd_list[i].fields.book_price + '</td><td>' +
                            prd_list[i].fields.book_date + '</td><td>' +
                            prd_list[i].fields.book_stock + '</td><td>' +
                            result.pubs_json[i].fields.pub_name + '</td></tr>'
                        )
                    };
                    $('#searched_result_table').append('</table>')
                };
            },
            error: function(){

            },
            complete: function(){

            }
        });
    });
});