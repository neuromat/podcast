$(document).ready(function(){
  $('#searchBtn').click(function(){
    $('#searchBoxContainer').css('display', 'flex');
  });

  $('#closeBtn').click(function(){
    console.log('close btn');
    $('#searchBoxContainer').fadeOut();
  });
})
