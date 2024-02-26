$(document).ready(function(){
    let $tabContent = $('#tabContent div');

    // 첫 번째 탭메뉴 항목 선택되어 있게 설정
    $('#tab li:first-child').addClass('selectedItem');   //파란색

    $('#tab li').on("click", function(){
        // 클릭한 탭 메뉴 항목 인덱스 알아오기
        let index = $(this).index();

        // 탭 메뉴 항목을 선택된 이미지로 변경
        // 모든 탭 메뉴 항목에 선택 시 적용된 css 효과 제거하고
        $('#tab li').removeClass('selectedItem');

        // 클릭한 항목에만 선택한 css 효과 설정 : 파란색
        $(this).addClass('selectedItem');

        // 컨텐츠 이미지 변경
        // 컨텐츠의 모든 div는 숨기고
        $tabContent.css('display', 'none');

        // 클릭한 탭 메뉴 항목만 index에 해당되는 div 보임
        $tabContent.eq(index).css('display', 'block');
    });
});