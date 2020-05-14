const $ = window.$;
$(document).ready(function () {
  $.ajax('https://fourtonfish.com/hellosalut/?lang=fr').done(function (data) {
    $('DIV#hello').text(data.hello);
  });
});
