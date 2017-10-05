'use strict'
$(function(){
    console.log('ready!')

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chat_socket = new WebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);

    $('#chatform').on('submit', function(e){
        var chat_from_client = {
            handle: $('#handle').val(),
            chat: $('#chat').val(),
        }
        chat_socket.send(JSON.stringify(chat_from_client));
        $(this).val('').focus();
        return false
    })

    chat_socket.onmessage = function (e) {
        var data = JSON.parse(e.data);
        // console.log('from server', data)
        $('#chat_table').append('<tr>'
            + '<td>' + data.timestamp + '</td>'
            + '<td>' + data.handle + '</td>'
            + '<td>' + data.chat + ' </td>'
            + '</tr>');
    };

})