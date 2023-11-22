function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 13.736694 , lng:100.531658},
    zoom: 14
    });
}
function calcRoute() {
    var start = document.getElementById('start').value;
    var end = document.getElementById('end').value;
    var request = {
      origin: start,
      destination: end,
      travelMode: 'DRIVING'
    };
    directionsService.route(request, function(result, status) {
      if (status == 'OK') {
        directionsRenderer.setDirections(result);
      }
    });
  }
function 