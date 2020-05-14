const $ = window.$;
$(document).ready(function () {
  function loadData () {
    const lang = $('INPUT#language_code').val();
    $.ajax('https://fourtonfish.com/hellosalut/?lang=' + lang).done(function (data) {
      $('DIV#hello').text(data.hello);
    });
  }

  $('INPUT#btn_translate').click(function () {
    loadData();
  });

  $('INPUT#language_code').on('keypress', function (e) {
    if (e.which === 13) {
      loadData();
    }
  });
});
