// Filtering.js
// by [beechnut](http://github.com/beechnut)
//
// 
// 

$(function() {

  $("form").change(function() {
    var str = $('form').serialize();
    str = str.replace(/[^&]+=\.?(?:&|$)/g, '')
    
    // Add posts into sidebar
    $.getJSON('map/get_blogs/?' + str, function(data) {
      $('#sidebar').empty();
      // TODO: Handle empty return object.
      $.each(data["posts"], function(key, val){
          $('#sidebar').append("<h2>" + val["title"] + "</h2>");
          $('#sidebar').append(val["text"]).addClass("sidebar-post");
      });
    });

  });

  $("#clear_button").on("click", function(){
    $('#sidebar').empty().append("Search for Peace Corps Volunteers.");
    $('form')[0].reset();
  });


  // Get country names for typeahead searchbox

  $.getJSON('map/get_data_options', function(data) {
    var countries = []
    $.each(data["data"]["countries"], function(key, val){
        countries.push(val[1]);
    });
    $('#searchbox').typeahead({source: countries});
  });

});