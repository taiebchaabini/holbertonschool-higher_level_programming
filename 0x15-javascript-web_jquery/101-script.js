const $ = window.$;
$(document).ready(function () {
  const myList = $('UL.my_list');
  $('DIV#add_item').click(function () {
    myList.append('<li>Item</li>');
  });
  $('DIV#remove_item').click(function () {
    myList.find(':last-child').remove();
  });
  $('DIV#clear_list').click(function () {
    myList.empty();
  });
});
