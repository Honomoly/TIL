$(document).ready(function(){
    function openArea(index){
        switch(index){
            case 0: location.href = "GaPyong.html"; break;
            case 1: location.href = "DanYang.html"; break;
            case 2: location.href = "GyongJu.html"; break;
            case 3: location.href = "DaeGu.html"; break;
            case 4: location.href = "BuSan.html"; break;
            case 5: location.href = "YeoSU.html"; break;
            case 6: location.href = "GoYang.html"; break;
            case 7: location.href = "JeJu.html"; break;
            case 8: location.href = "SoonCheon.html"; break;
            case 9: location.href = "TeAn.html"; break;
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