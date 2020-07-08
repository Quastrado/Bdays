

$(document).ready(function () {
  // $('#imagePicker').click(function () {
  //   console.log($)
  //   $.FileDialog({ multiple: false }).on('files.bs.filedialog', function (ev) {
  //     var file = ev.file;
  //     console.log(file);
  //   });
  // });

  $('#personalArea').hide();
  $('#errorAlert').hide();
  var $body = $('body');

  $body.on('click', 'div.master_list div.list-group button', function () {
    var $button = $(this),
      article_option = $button.attr('data-option');
    console.log(article_option)
    $.ajax({
      type: 'GET',
      url: "/studio_member/" + article_option,
      success: function (data) {
        $('#content').html(data);
      },
    });
  });
});

$('#newStudioMemberSubmit').click(function () {
  var email = $('#emailInput').val();
  var nickname = $('#nicknameInput').val();
  var birthday = $('#birthdayInput').val();
  var role = $('#rolesDropdown').children('option:selected').val()
  var data = {
    email: email,
    nickname: nickname,
    birthday: birthday,
    role: role
  }
  console.log(data);
  $.ajax({
    url: "/studio_member/",
    type: 'POST',
    contentType: "application/json; charset=utf-8",
    data: JSON.stringify(data),
    error: function (response) {
      console.log(response)
      $('#alertText').text(response.status + ' ' + response.responseText);
      $('#errorAlert').fadeIn('slow');

    }

  });
});


$('#editProfile').click(function () {
  $('#dashboard').hide();
  $('#personalArea').show();
});


$('#personalAreaClose').click(function () {
  $('#personalArea').hide();
  $('#dashboard').show();
});



// GET запрос - получить с сервера
// POST запрос - отдать на сервер
// необходим роут, который примет запрос. В контроллере для studio_members 

