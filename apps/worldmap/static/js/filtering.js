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
    var body = post["body"];
    var preview = body.substr(0, 150) + "...";
    preview = preview + "<a onclick=''>Read more</a>";
    return preview;
  }


  // Form partial

  $.postpartial = function(post) {
    var name = post.author.username;
    var title = post.title;

    var partial = "<br/><br/><div class='sidebar-post'>";
    partial = partial + "<span class='post-title'>" + title + "</span><br/>";
    partial = partial + "<span class='post-byline'>by <a href='" + name + "'>" + name + "</a> on " + $.date(post["post_time"]) + "</span><br/>";
    partial = partial + "<span class='post-body'>" + $.postpreview(post) + "</span>";
    return partial;
  }


  // Get country names for typeahead searchbox & geo lookup

  var dict = []
  $.getJSON('map/get_data_options', function(data) {
    var countries = []

    $.each(data["data"]["countries"], function(key, val){
      var object = {"code": val["code"], "coords": val["coords"], "zoomlevel": val["zoomlevel"]};
      dict.push(object);
      countries.push(val["name"]);
    });
    $('#searchbox').typeahead({source: countries});
  });


  // Updates results based on form parameters

  $.updatePosts = function(){
    var str = $('form').serialize();
    str = str.replace(/[^&]+=\.?(?:&|$)/g, '') // Strip out blank params

    // Add posts into sidebar
    $.getJSON('map/get_blogs/?' + str, function(data) {
      $('#sidebar').empty();
      if (data["objects"].length == 0){
        $('#sidebar').append("<br/><br/>No blog entries matched your search. Clear the search and try again.");
      }

      // Display in sidebar a partial for each post
      $.each(data["objects"], function(index,post){
        $('#sidebar').append($.postpartial(post));
      });
      var country = data["objects"][data["objects"].length-1].author.country;
      $.updateMap();
    });

  }

  $.updateMap = function(){
    var datagood = $.grep(dict, function(n) {
      return n.code == $('select#country option:selected').val();
    });
    var country = datagood[0];
    var coords = country.coords;
    var lng = coords[0];
    var lat = coords[1];
    var zoomlevel = country.zoomlevel - 2;

    map.center({ lon: lng, lat: lat });
    map.zoom(zoomlevel);
  }


  // Update posts on page load

  $.updatePosts();


  // Update posts when a field is changed or search box is submitted

  $("form").change(function() {
    $.updatePosts();
    $.updateMap();
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




});