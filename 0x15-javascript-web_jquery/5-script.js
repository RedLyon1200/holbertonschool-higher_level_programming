$('#add_item').click(function () {
  const list = $('ul.my_list');
  if (list) {
    list.append('<li>Item</li>');
  }
});
