$(document).ready(function () {
  $('INPUT#btn_translate').click(function () {
    const lang = $('INPUT#language_code').val();
    const url = 'https://www.fourtonfish.com/hellosalut/hello/';
    $.get(url, { lang }, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
