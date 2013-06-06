// Filtering.js
// by [beechnut](http://github.com/beechnut)
//
// 
// 

$(function() {

  $("form").change(function() {
    var str = $("form").serialize();
    alert(str); // Just for debugging purposes right now.

    // Add posts into sidebar
    $.getJSON('map/get_blogs', function(data) {   // add { query: str } once working
      $('#sidebar').empty();
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