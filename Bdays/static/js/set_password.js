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
    $('#setPasswordForm').hide();
    $('#setPasswordFinish').show();
})