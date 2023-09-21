$(document).ready(function(){
    function openArea(index){
        switch(index){
            case 0: location.href = "../area/GaPyong.html"; break;
            case 1: location.href = "../area/DanYang.html"; break;
            case 2: location.href = "../area/GyongJu.html"; break;
            case 3: location.href = "../area/DaeGu.html"; break;
            case 4: location.href = "../area/BuSan.html"; break;
            case 5: location.href = "../area/YeoSU.html"; break;
            case 6: location.href = "../area/GoYang.html"; break;
            case 7: location.href = "../area/JeJu.html"; break;
            case 8: location.href = "../area/SoonCheon.html"; break;
            case 9: location.href = "../area/TeAn.html"; break;
        }
    }
    $('.area_btn').each(function(index){
        $(this).on('click',function(){
            openArea(index);
        });
    });
    $('.sub_btn').each(function(index){
        $(this).on('click',function(){
            openArea(index);
        });
    });
    
});