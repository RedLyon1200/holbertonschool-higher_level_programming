$(function () {
  $('#btn_translate').click(function () {
    const url = 'https://fourtonfish.com/hellosalut/?lang=' + $('#language_code').val();
    $.get(url, function (data) {
      if (data.code !== 'none') {
        $('#hello').text(data.hello);
      } else {
        $('#hello').text('Language code not found');
      }
    });
  });
});
