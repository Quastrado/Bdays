$('#enterPassword').on('keyup', function(){
    var val = $(this).val();
    if (val.length != 0)
    {
        $('#repeatPassword').fadeIn('slow');
    }
    else
    {
        $('#repeatPassword').fadeOut('slow');
        $('#setPasswordButton').fadeOut('slow');
    }
})

$('#repeatPassword').on('keyup', function(){
    var password = $('#enterPassword').val();
    var val = $(this).val();
    if ((val.length != 0) && (val == password))
    {
        $('#setPasswordButton').fadeIn('slow');
    }
    else
    {
        $('#setPasswordButton').fadeOut('slow');
    }
})

$('#setPasswordButton').click(function() {
    var id = $('#setPasswordFinish').attr('data-studioMemberId');
    var password = $('#enterPassword').val();
    var data = {
        id: id,
        password: password
    }
    $.ajax({
        url: "/studio_member/set_password",
        type: 'POST',
        contentType: "application/json; charset=utf-8",
        data: JSON.stringify(data),
        success: function(){
            $('#setPasswordForm').hide();
            $('#setPasswordFinish').show();
        }
    })
})