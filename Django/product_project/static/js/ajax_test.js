$(document).ready(function(){
    $('#test_form').on('submit', function(){
        event.preventDefault();
        // Ajax가 나설 차례
        let input_data = $(this).serialize()
        $.ajax({
            type: 'post',
            data: input_data,
            url: '/product_get_data/',
            datatype: 'json',
            success: function(result){
                // 성공시 가져온 result를 가지고 수행할 명령
                console.log(result.input_data)
                $('#result_box').html("<p>"+result.input_data+"</p>")
            },
            error: function(){
                // 오류 발생하면 실행할 명령
                alert('오류 발생')
            },
            complete: function(){

            }
        });
    });
    $('#btn2').on('click', function(){
        event.preventDefault();
        // Ajax가 나설 차례
        let input_data = $(this).serialize()
        $.ajax({
            type: 'post',
            data: input_data,
            url: '/product_get_data/',
            datatype: 'json',
            success: function(result){
                // 성공시 가져온 result를 가지고 수행할 명령
                console.log(result.input_data)
                $('#result_box').html("<p>"+result.input_data+"</p>")
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