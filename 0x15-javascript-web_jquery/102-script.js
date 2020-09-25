$(function () {
  $('input#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('input#language_code').val();
    $.get(url, function (data) {
      if (data.code !== 'none') {
        $('input#hello').text(data.hello);
      } else {
        $('input#hello').text('Language code not found');
      }
    });
  });
});
