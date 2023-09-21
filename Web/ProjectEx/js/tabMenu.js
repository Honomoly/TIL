$(function(){
    let $tabContent = $('#tabContent div');

    // 디폴트는 첫 메뉴
    $('#tab li:first-child').addClass('selectedItem');
    // class="selectedItem"이 됨으로서 css 적용이 가능해짐

    $('#tab li').on('click', function(){
        let index = $(this).index(); // 클릭된 녀석의 인덱스 알아오기
        $('#tab li').removeClass('selectedItem');
        $(this).addClass('selectedItem');
        $tabContent.css('display', 'none');
        $tabContent.eq(index).css('display', 'block');
    });
});