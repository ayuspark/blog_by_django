'use strict'

$(function () {
    console.log("ready!");

    function validateEmail(email) {
        var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
        return re.test(email);
    }
    
    // check if password matches
    $('#id_confirm_psw').keyup(function(){
        let confirm_psw = $(this).val(), psw=$('#id_psw').val();
        if(psw === confirm_psw){
            $('#id_confirm_psw').css('background-color', '#F0FFF0');
        } else {
            $('#id_confirm_psw').css('background-color', '#FFE4E1');
        }
    })

    // check is email is registered
    $('#id_email').change(function(){
        let email = $(this).val();
        if(validateEmail(email)){
            $.ajax({
                url: '/register/check_email',
                data: {
                    'email': email,
                },
                dataType: 'json',
                success: function(response){
                    if(response.exists){
                        $('#id_email + span').remove();
                        $('#id_email').after("<span class='alert alert-danger' role='alert'>Email exists</span>").css('background-color', '#FFE4E1');
                    } else {
                        $('#id_email + span').remove();
                        $('#id_email').after("<span class='glyphicon glyphicon-ok'></span>").css('background-color', '#F0FFF0');
                    }
                }
           })
        } else {
            $(this).after("<span class='alert'>Invalid email</span>").css('background-color', '#FFE4E1')
        }
    })


});
