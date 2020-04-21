$(document).ready(function() {
    $('form').on('submit', function(event){
        var data = {
            username: $('#usernameInput').val(),
            password: $('#passwordInput').val()
            };
        
    $.ajax({
        type: 'POST',
        url: '/login/process-login',
        data: data,
        success: function(response){
            console.log(response)
            // if ( response=== 302){
            //     console.log('yep')
            //     window.location.href = '/dashboard';
            //     }
            window.location.href = response;
            } 
        });
        event.preventDefault();    
    });
});