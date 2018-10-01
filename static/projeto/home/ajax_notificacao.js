$(document).ready(function(){
    $.ajax({
        type: 'GET',
        url: '/usuario/minhas_notificacoes/',
        dataType: "json",
        success: function(data){
            // debugger
            $('.notification_num').append(data[0]);
            for ( i = 0 ; i < data.length ; i++ ) {
                if ( i > 0 ) {
                    $('.drop_field_notify').append('<li><a href="/usuario/notify_view/'+data[i][1]+'">'+data[i][0]+'</a></li>');
                }
            }
        }
    });
});