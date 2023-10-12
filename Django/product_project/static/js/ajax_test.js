$(document).ready(function(){
    $('#get_data_btn').on('click', function(){
        // Ajax가 나설 차례
        $.ajax({
            url: '/product_get_data/',
            datatype: 'json',
            success: function(result){
                // 성공시 가져온 result를 가지고 수행할 명령
                $('#result_box').text(result.name)
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