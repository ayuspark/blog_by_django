'use strict'
$(function(){
    console.log('ready!')

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


})