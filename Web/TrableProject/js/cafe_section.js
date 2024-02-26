$(function(){
    let time_itv = 400;
    let $cafe = $('section div:first-child');
    let ind = 0;
    function openFade() {
        $cafe.fadeTo(time_itv, 1,).animate({bottom: 0}, time_itv);
        $cafe = $cafe.next();
        ++ind;
        if (ind==5) clearInterval();
    }
    setInterval(openFade, time_itv);  

    $('tfoot.cafe_info a')
        .on('mouseover', function(){
            $(this).stop().animate({top: 16}, 180);
        })
        .on('mouseout', function(){
            $(this).stop().animate({top: 20}, 180);
        });
});