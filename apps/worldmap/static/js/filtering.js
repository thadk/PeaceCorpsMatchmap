// Filtering.js
// by [beechnut](http://github.com/beechnut)
//
// 
// 

$(function() {

  $("form").change(function() {
    var str = $("form").serialize();
    alert(str);
  });

  $.getJSON('map/get_data_options', function(data) {
    var countries = []
    $.each(data["data"]["countries"], function(key, val){
        countries.push(val[1]);
    });
    $('#searchbox').typeahead({source: countries});
  });

});