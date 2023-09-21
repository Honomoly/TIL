$(document).ready(function(){
    $('#id').focus();

    // 휴대폰 번호 입력 자동 넘어가기
    $('#hp1').on('keyup', function(){ // 첫 칸에 커서가 있을 때
        if ($(this).val().length==3){ // 입력값이 3자리가 되면
            $('#hp2').focus(); // 다음칸으로 커서 이동
        }
    });
    $('#hp2').on('keyup', function(){
        if ($(this).val().length==4){
            $('#hp3').focus();
        }
    });

    /*
    Enter의 디폴트는 submit이기 때문에 그렇지 않도록 조치한다
    Enter키의 ASCII 코드값은 13이다
    */
    $(document).on('keydown', function(e){
        if(e.keyCode==13) return false;
    });

    // 엔터키 눌렀을 시 포커스 이동
    $('#id').on('keydown', function(e){
        if($('#id').val()!='' && e.keyCode == 13){
            $('#pwd').focus();
        }
    });

    $('#newMemberForm').on('submit', function(){
        // 아이디 입력
        if ($('#id').val()==''){
            alert('아이디를 입력하세요')
            $('#id').focus();
            return false;
        }

        // 라디오 버튼 입력
        if (!$('input[type="radio"]').is(':checked')){
            alert('학년을 선택하세요')
            return false;
        }

        // 체크박스 입력
        // if (!$('input[type="checkbox"]').is(':checked')){
        if (!$(':checkbox').is(':checked')){
            alert('관심분야를 선택하세요')
            return false;
        }
    });
});