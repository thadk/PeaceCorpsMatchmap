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

  var countries = ["Albania", "Armenia", "Azerbaijan", "Belize", "Benin", 
                  "Botswana", "Bulgaria", "Burkina Faso", "Cambodia", "Cameroon", 
                  "Cape Verde", "China", "Colombia", "Costa Rica", "Dominican Republic", 
                  "Eastern Caribbean", "El Salvador", "Ecuador", "Ethopia", "Fiji", 
                  "Georgia", "Ghana", "Guatemala", "Guinea", "Guyana", "Honduras", 
                  "Indonesia", "Jamaica", "Jordan", "Kazakhstan", "Kenya", 
                  "Kyrgyz Republic", "Lesoto", "Liberia", "Macedonia", "Madagascar", 
                  "Malawi", "Mali", "Mexico", "Micronesia and Polynesia", "Moldova", 
                  "Mongolia", "Morocco", "Mozambique", "Namibia", "Nepal", "Nicaragua", 
                  "Niger", "Panama", "Paraguay", "Peru", "Philipines", "Romania", 
                  "Rwanda", "Samoa", "Senegal", "Sierra Leone", "South Africa", 
                  "Suriname", "Swaziland", "Tanzania", "The Gambia", "Thailand", 
                  "Togo", "Tnoga", "Uganda", "Ukraine", "Vanatu", "Zambia"];

  $('#searchbox').typeahead({source: countries});

});