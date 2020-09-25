$(function () {
  function translateHello () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
    $.get(url, function (data) {
      if (data.code !== 'none') {
        $('#hello').text(data.hello);
      } else {
        $('#hello').text('Language code not found');
      }
    });
  }

  $('#btn_translate').click(translateHello);
  $('#language_code').keypress(function (event) {
    if (event.keyCode === 13) {
      translateHello();
    }
  });
});
