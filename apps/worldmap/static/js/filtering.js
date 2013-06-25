// filtering.js
// by [beechnut](http://github.com/beechnut)
//
//
//

$(function() {  // On document ready


  // Date helper to format returned date

  $.date = function (dateObject) {
    var d = new Date(dateObject);
    var day = d.getDate();
    var month = d.getMonth();
    var year = d.getFullYear();
    var date = year + "." + month + "." + day;

    return date;
  }


  // Truncate the post body text

  $.postpreview = function(post) {
    var p = post["text"];
    var preview = p.substr(0, 150) + "...";
    preview = preview + "<a onclick=''>Read more</a>";
    return preview;
  }


  // Form partial

  $.postpartial = function(post) {
    var name = post["user"]["username"]
    var title = post["title"]

    var partial = "<br/><br/><div class='sidebar-post'>";
    partial = partial + "<span class='post-title'>" + title + "</span><br/>";
    partial = partial + "<span class='post-byline'>by <a href='" + name + "'>" + name + "</a> on " + $.date(post["date"]) + "</span><br/>";
    partial = partial + "<span class='post-body'>" + $.postpreview(post) + "</span>";
    return partial;
  }


  // Updates results based on form parameters

  $.updatePosts = function(){
    var str = $('form').serialize();
    str = str.replace(/[^&]+=\.?(?:&|$)/g, '') // Strip out blank params

    // Add posts into sidebar
    $.getJSON('map/get_blogs/?' + str, function(data) {
      $('#sidebar').empty();
      if (data["posts"].length == 0){
        $('#sidebar').append("<br/><br/>No blog entries matched your search. Clear the search and try again.");
      }b
      // TODO: Handle country or profile header object.
      if (data["header"]) {
        alert("Got header!:" + data["header"]);
      }
      // Display in sidebar a partial for each post
      $.each(data["posts"], function(key, post){
          $('#sidebar').append($.postpartial(post));
      });
    });

    $.initializeMap = function(){
      // mapbox.auto('map', 'matchmap.map-7egeornz');
      var map = mapbox.map('map');
      map.addLayer(mapbox.layer().id('matchmap.map-7egeornz'));
      map.zoom(6).center({lon: 42, lat: -71});
    }
  }

  // Update posts on page load

  $.initializeMap();
  $.updatePosts();

  // Update posts when a field is changed or search box is submitted

  $("form").change(function() {
    $.updatePosts();
  });

  $("form").submit(function(event) {
    event.preventDefault();
    $.updatePosts();
  });

  // Clear posts when "Clear Search" button is clicked.

  $("#clear_button").on("click", function(){
    $('#sidebar').empty().append("<br/><br/>Search for Peace Corps Volunteers.");
    $('form')[0].reset();
  });

  $("#toggle_active").on("click", function(){
    $('#sidebar').toggleClass("active");
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