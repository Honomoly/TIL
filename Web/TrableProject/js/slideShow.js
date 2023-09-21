$(document).ready(function(){
    let movedIndex = 0;

    function moveSlide(index){
        // 전달받은 Index 값을 현재 위치 변수에 저장
        movedIndex = index;

        // 슬라이드 이동
        let moveLeft = -(index * 1280); // 왼쪽으로 이동 거리
        $('#slidePanel').animate({'left':moveLeft}, 'slow');
    }

    // prevButton 클릭했을 때
    $('#prevButton').on("click", function(){
        if(movedIndex != 0){
            movedIndex = movedIndex -1;
        }

        moveSlide(movedIndex);
    });

    // nextButton 클릭했을 때
    $('#nextButton').on("click", function(){
        if(movedIndex != 4){
            movedIndex = movedIndex +1;
        }

        moveSlide(movedIndex);
    });

    // 초기 슬라이드 이미지 랜덤하게 출력
    let randomNum = Math.floor(Math.random() * 5);
    moveSlide(randomNum);

    // 마우스 올렸을 때 이미지 변경(1 -> 2)
    // 각 컨트롤 버튼에 대해

    $('.controlButton').each(function(index){
        $(this).hover(
            function(){
                $(this).attr('src', 'image/controlButton2.png');
            },
            function(){
                $(this).attr('src', 'image/controlButton1.png');
            }
        );

        // 클릭했을 때 moveSlide() 함수 호출하면서 index 전달
        $(this).on("click", function(){
            moveSlide(index);
        });

    });
});