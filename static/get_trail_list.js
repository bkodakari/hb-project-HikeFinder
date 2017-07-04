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
  for (var i=0; i < arrayTrailNames.length; i++){
  console.log(arrayTrailNames[i]);
  document.getElementById('json_of_hikes').innerHTML += ('<li>'+'<a href="/trails/'+data[arrayTrailNames[i]][5]+'"">'+arrayTrailNames[i]+'</a></li>');
}
}
// var lat = data[arrayTrailNames[i]][1]
// var lng = data[arrayTrailNames[i]][2]
