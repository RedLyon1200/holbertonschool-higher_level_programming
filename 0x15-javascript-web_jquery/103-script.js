$(function () {
  function translateHello () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('input#language_code').val();
    $.get(url, function (data) {
      if (data.code !== 'none') {
        $('div#hello').text(data.hello);
      } else {
        $('div#hello').text('Language code not found');
      }
    });
  }

  $('input#btn_translate').click(translateHello);
  $('input#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
