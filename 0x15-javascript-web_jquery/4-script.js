$('#toggle_header').click(function () {
  const header = $('header');

  header.toggleClass('green');
  header.toggleClass('red');
});
