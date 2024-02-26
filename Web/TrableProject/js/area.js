$(document).ready(function(){
    $('.area_sel').each(function(index){
        function showArea(index){
            $('#area1').css('display', 'none');
            $('#area2').css('display', 'none');
            $('#area3').css('display', 'none');
            $('#area4').css('display', 'none');
            $('#area5').css('display', 'none');
            $('#prevButton1').css('display', 'block');
            $('#prevButton2').css('display', 'block');
            $('#nextButton1').css('display', 'block');
            $('#nextButton2').css('display', 'block');
            $('#area' + (index + 1)).css('display', 'block');
        }
        function showMenu(){
            $('#showAllMenu').on('click',function(){
                if($(this).text() == '전체보기'){
                    $('#area_sub_menu').css('visibility','visible');
                    $(this).text('메뉴닫기');
                }else{
                    $('#area_sub_menu').css('visibility','hidden');
                    $(this).text('전체보기');
                }
            });
        }
        $(this).on('mouseover', function(){
            $(this).css('color', 'red');
        }).on('mouseout', function(){
            if (!$(this).hasClass('selected')) {
                $(this).css('color', 'black');
            }
        }).on('click', function(){
            $('.area_sel').removeClass('selected');
            $(this).addClass('selected');

            if(index != 5)
                showArea(index);
            else if(index == 5)
                showMenu();

            $('#tab li a').css('color','black');
            $(this).css('color','red'); 
        });
    });
});