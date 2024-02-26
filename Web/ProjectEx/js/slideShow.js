$(function(){
    let movedIndex = 0;

    function moveSlide(index) {
        movedIndex = index;
        let moveLeft = -(index*1280);
        $('#slidePanel').animate({left: moveLeft}, 'slow');
    };

    $('#prevButton').on('click', function(){
        if(movedIndex != 0) {
            movedIndex -= 1;
            moveSlide(movedIndex);
        } else {
            moveSlide(4);
        };
    });

    $('#nextButton').on('click', function(){
        if(movedIndex != 4) {
            movedIndex += 1;
            moveSlide(movedIndex);
        } else {
            moveSlide(0);
        };
    });

    // 마우스를 올릴 때
    $('.controlButton').each(function(index){
        $(this).hover(function(){
            $(this).attr('src', 'image/controlButton2.png');
        },
        function(){
            $(this).attr('src', 'image/controlButton1.png');
        });
    });

    // 마우스를 클릭할 때
    $('.controlButton').each(function(index){
        $(this).on('click', function() {
            moveSlide(index);
        });
    });
});