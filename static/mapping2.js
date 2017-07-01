
// var map;
// function initMap() {
//   map = new google.maps.Map(document.getElementById('map'), {
//     center: {lat: 37.7749, lng: -122.4194},
//     zoom: 8
//   });
// }



window.onload = function () {
  var lat=$('#43287').data('lat');
  console.log(lat);
  var lng=$('#43287').data('lng');
  console.log(lng);
  var myLatLng = {lat: lat, lng: lng};
  console.log(myLatLng);

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 8,
    center: myLatLng
  });

  var marker = new google.maps.Marker({
    position: myLatLng,
    map: map,
    title: 'Hello World!'
  });
}