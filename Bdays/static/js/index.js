

$(document).ready(function () {
    var $body = $('body');
  
    $body.on('click', 'div.master_list div.list-group button', function () {
      var $button = $(this),
        article_option = $button.attr('data-option');
        console.log(article_option)
      $.ajax({
        type: 'GET',
        url: "/studio_member/" + article_option,
        success: function(data){
          $('#content').html(data);
        },
      });
    });
   });
// GET запрос - получить с сервера
// POST запрос - отдать на сервер
// необходим роут, который примет запрос. В контроллере для studio_members 

