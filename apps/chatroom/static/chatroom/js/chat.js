'use strict'
$(function(){
    console.log('ready!')

    var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
    var chat_socket = new WebSocket(ws_scheme + '://' + window.location.host + "/chat" + window.location.pathname);

    $('#chatform').on('submit', function(e){
        var chat = {
            handle: $('#handle').val(),
            chat: $('#chat').val(),
        }
        chat_socket.send(JSON.stringify(chat));
        return false
    })

    chat_socket.onmessage = function (message) {
        var data = JSON.parse(message.data);
        $('#chat').append('<tr>'
            + '<td>' + data.timestamp + '</td>'
            + '<td>' + data.handle + '</td>'
            + '<td>' + data.message + ' </td>'
            + '</tr>');
    };

})