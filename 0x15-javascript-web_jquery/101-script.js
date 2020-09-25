(function () {
  document.addEventListener('DOMContentLoaded', function () {
    const list = $('ul.my_list');
    // Add item in list
    $('div#add_item').click(function () {
      list.append('<li>Item</li>');
    });

    // Remove item in list
    $('div#remove_item').click(function () {
      const li = $('ul.my_list li');
      li[li.length - 1].remove();
    });

    // Clear list
    $('div#clear_list').click(function () {
      list.empty('li');
    });
  }, false);
})();
