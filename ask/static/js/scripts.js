/**
 * Created by snake on 11/16/13.
 */

/*
$('#navtabs li').click(function(){
        $(this).parents('#feed-nav').children('li').removeClass('active');
        $(this).addClass('active');
    });
*/

function setupCsrfAjax() {
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        crossDomain: false, // obviates need for sameOrigin test
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}



jQuery(Document).ready(function(){
    setupCsrfAjax();

    $.toast.config.align = 'right';
    $.toast.config.closeForStickyOnly = false;
    $.toast.config.width = 300;



    $('.rating_button').click(function(){

        var c = $(this).parents(".content_block");
        var cid = c.data("id");
        var votetype = $(this).data("votetype");
        var content_type = $(this).data("contenttype");

        $.ajax({
                    type: "post",
                    url: "vote",
                    data:
                    {
                        c_id: cid,
                        contenttype: content_type,
                        votetype: votetype
                    }
                })
            .done(function(msg){

                        if (msg["error"] != null)
                        {
                            $.toast(msg['error'], {duration: 2000, type: 'danger'});
                            return;
                        }
                        $.toast(msg['result'], {duration: 2000, type: 'success'})
                        c.find(".rating-table").text(msg["rating"]);
                        })
            .fail(function(msg){
                    alert(msg["result"]);
                });
            return false;
            });

    $('.correct_button').click(function(){
        var c = $(this).parents(".content_block");
        var cid = c.data("id");

        $.ajax({
                    type: "post",
                    url: "ans_correct",
                    data:
                    {
                        c_id: cid
                    }
                })
            .done(function(msg){

                        if (msg["error"] != null)
                        {
                            $.toast(msg['error'], {duration: 2000, type: 'danger'})
                            return;
                        }
                        $.toast(msg['result'], {duration: 2000, type: 'success'})
                        if (msg["toggle"] == true)
                        {
                            c.addClass('alert-success');
                            c.find(".correct_toggle").removeClass('icon-ok');
                            c.find(".correct_toggle").addClass('icon-remove');
                        }
                        else
                        {
                            c.removeClass('alert-success');
                            c.find(".correct_toggle").removeClass('icon-remove');
                            c.find(".correct_toggle").addClass('icon-ok');
                        }
                        })
            .fail(function(msg){
                    alert(msg["result"]);
                });
            return false;
            });
    });