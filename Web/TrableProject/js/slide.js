$(document).ready(function(){
    let movedIndex = 0;
    function moveSlide(index){
        movedIndex = index;
        let moveLeft = -(index * 800);
        $('.subArea1').animate({'left': moveLeft},'slow');
    }
    $('#prevButton1').on('click',function(){
        if(movedIndex != 0){
            movedIndex = movedIndex - 1;
        }
        moveSlide(movedIndex);
    });

    $('#nextButton1').on('click',function(){
        if(movedIndex != 1){
            movedIndex = movedIndex + 1;
        }
        moveSlide(movedIndex);
    });
});
$(document).ready(function(){
    let movedIndex = 0;
    function moveSlide(index){
        movedIndex = index;
        let moveLeft = -(index * 800);
        $('.subArea2').animate({'left': moveLeft},'slow');
    }
    $('#prevButton2').on('click',function(){
        if(movedIndex != 0){
            movedIndex = movedIndex - 1;
        }
        moveSlide(movedIndex);
    });

    $('#nextButton2').on('click',function(){
        if(movedIndex != 1){
            movedIndex = movedIndex + 1;
        }
        moveSlide(movedIndex);
    });
});