$(document).ready(function(){
    $('#prdSearchForm3').on('submit', function(){
        // 새로고침 막기
        event.preventDefault();

        // 폼에 입력한 값을 쿼리 스트링으로 변환
        // serialize() 메소드 사용
        // ex) type=prd_name&keyword=자전거
        let form_data = $(this).serialize();

        $.ajax({ // 데이터 통신
            type: 'post', // 보내는 데이터 형식
            url: '/product_search3/', // 데이터를 보낼 주소
            data: form_data, // 보내는 데이터
            datatype: 'json', // 보내는 데이터 타입
            success: function(result){
                $('#searchResultBox3').html(result);
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