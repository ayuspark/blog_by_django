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
        });
        console.log('msg form', $('.leave_msg_form')[0]);
        $('.leave_msg_form')[0].reset();
    })

    $('.msg_wall').on('submit', 'form',function(e){
        e.preventDefault();
        let $curr_div_id = $(this).attr('div_id'), select_id = '';
        $.ajax({
            url: $(this).attr('action'),
            method: 'post',
            data: $(this).serialize(),
            success: function(response){
                select_id = '#' + $curr_div_id;
                console.log('sele',select_id);
                $(select_id).append(response);
            }
        });
        // does not work
        $(this).reset();
    })


})