
// var map;
// function initMap() {
//   map = new google.maps.Map(document.getElementById('map'), {
//     center: {lat: 37.7749, lng: -122.4194},
//     zoom: 8
//   });
// }



function initMap() {
  var myLatLng = {lat: $('#856').data('lat'), lng: $('#856').data('lng')};

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 4,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}