$('#add_item').click(function () {
  const list = $('UL.my_list');
  if (list) {
    list.append('<li>Item</li>');
  }
});
