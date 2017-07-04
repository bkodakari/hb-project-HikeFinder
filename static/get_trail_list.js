$('#submit').on('click', getList);

function getList(evt){
  evt.preventDefault();
  console.log("*******do something, please");
  var formInputs = {
    'address':$('#address').val(),
    'distance':$('#distance').val()};
  $.get('/local-hikes', formInputs, loadListOfHikes);
}

function loadListOfHikes(data){
  var arrayTrailNames = [];
  $.each(data, function(key, value){
    arrayTrailNames.push(key);
  });
  console.log(data);
  
  var arrayTrailLatLng = [];

  for (var i=0; i < arrayTrailNames.length; i++){
  console.log(arrayTrailNames[i]);
  var lat = data[arrayTrailNames[i]][1];
  var lng = data[arrayTrailNames[i]][2];
  var latLng = new google.maps.LatLng(lat, lng);
  console.log(latLng);
  arrayTrailLatLng.push(latLng);
  document.getElementById('json_of_hikes').innerHTML += ('<li>'+'<a href="/trails/'+data[arrayTrailNames[i]][5]+'"">'+arrayTrailNames[i]+'</a></li>');
  }

  console.log(arrayTrailLatLng);

  for (var l=0; l < arrayTrailLatLng.length; li++){
    var marker = new google.maps.Marker({
    position: arrayTrailLatLng[l],
    title:"Hello World!"
  });
  }

}




function initMap() {

  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 9,
    center: {lat: 37.7749, lng: -122.4194}
  });
}
