const $ = window.$;
$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    $.ajax('https://fourtonfish.com/hellosalut/?lang=' + lang).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
