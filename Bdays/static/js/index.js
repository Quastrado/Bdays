$(document).ready(function () {
    var $body = $('body');
  
    $body.on('click', 'div.master_list div.list-group button', function () {
      var $button = $(this),
        article_option = $button.attr('data-option');
        console.log(article_option)
      //   article_selector = 'article.' + article_option,
      //   $master_detail = $button.closest('.master_detail'),
      //   $article = $master_detail.find(article_selector);
  
      // $master_detail.find('article').removeClass('grow fadeIn');
  
      // $article.addClass('grow fadeIn');
      // ajax({
      //   type: 'GET',
      //   url: "/studio_member/uid",

      // })
    });
   });
// GET запрос - получить с сервера
// POST запрос - отдать на сервер
// необходим роут, который примет запрос. В контроллере для studio_members 
