const $ = window.$;
$(document).ready(function () {
  $('DIV#update_header').click(function () {
    $('header').html('New Header!!!');
  });
});
