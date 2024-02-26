$(function(){
    $(window).on('scroll', function(){
        // 전체문서(document)의 상단이 headerBox(화면의 상단) 위에 있으면 메인메뉴가 고정되기
        if($(document).scrollTop()>=$('#headerBox').height()){
            $('#slideShow')
            $('#mainMenuBox').addClass('mainMenuFixed', 'mainMenuShadow')
        } else {
            $('#mainMenuBox').removeClass('mainMenuFixed', 'mainMenuShadow')
        }
    });

    $('#moveToTop').on('click', function(){
        $('html, body').animate({scrollTop:0}, 500);
    })
});