/**
 * Created by snake on 11/16/13.
 */

$('#navtabs li').click(function(){
        $(this).parents('#feed-nav').children('li').removeClass('active');
        $(this).addClass('active');
    });