$(document).ready(function() {
    $('form').on('submit', function(event){
        var data = {
            username: $('#usernameInput').val(),
            password: $('#passwordInput').val(),
            password_replay: $('#passwordReplayInput').val()
        }
    
        $.ajax({
            type: 'POST',
            url: '/login/process-registration',
            data: data,
            success: function(response){
                console.log(response)
                window.location.href = response;
            },
        });
        event.preventDefault();
    });
});