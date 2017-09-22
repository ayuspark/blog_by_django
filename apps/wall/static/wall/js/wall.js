'use strict'
$(function(){
    console.log('ready!')

    // hide comment_form on pageload
    $('.comment_form').hide();
    $('.msg_section').hover(function(){
        $(this).find('form').slideDown({
            duration: 400,
            complete: function(){
                $(this).find('textarea').focus();
            }
        })
    }, function(){
        $(this).find('form').slideUp('slow');
    })

    $('.leave_msg_form').on('submit', function(e){
        e.preventDefault();
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function(response){
                $('.msg_wall').prepend(response);
            }
        })
    })

    $('.comment_form').on('submit', function(e){
        e.preventDefault();
        let comment_div = $(this);
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function(response){
                comment_div.prepend(response);
            }
        })
    })


})