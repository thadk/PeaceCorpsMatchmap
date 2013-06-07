// Filtering.js
// by [beechnut](http://github.com/beechnut)
//
// 
// 

$(function() {

  $("form").change(function() {
    var str = $('form').serialize();
    str = str.replace(/[^&]+=\.?(?:&|$)/g, '')
    //str = "gradelevel=4";
    alert(str); // Just for debugging purposes right now.

    // Add posts into sidebar
    $.getJSON('map/get_blogs/?' + str, function(data) {
      $('#sidebar').empty();
      // TODO: Handle empty set.
      $.each(data["posts"], function(key, val){
          $('#sidebar').append("<h2>" + val["title"] + "</h2>");
          $('#sidebar').append(val["text"]).addClass("sidebar-post");
      });
    });

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