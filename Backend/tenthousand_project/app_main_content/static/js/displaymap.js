function initMap() {
  var map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 13.736694 , lng:100.531658},
    zoom: 14
  });

  var directionsService = new google.maps.DirectionsService();
  var directionsDisplay = new google.maps.DirectionsRenderer({
      map: map
  });

  function calculateAndDisplayRoute(startLatitude, startLongitude, end) {
      var request = {
          origin: {lat: startLatitude, lng: startLongitude},
          destination: end,
          travelMode: 'DRIVING'
      };

      directionsService.route(request, function (response, status) {
          if (status == 'OK') {
              directionsDisplay.setDirections(response);
          }
      });
  }

  var buttons = document.querySelectorAll('.showRouteButton');
  buttons.forEach(function(button) {
      button.addEventListener('click', function() {
          var startLatitude = parseFloat(this.dataset.lat);
          var startLongitude = parseFloat(this.dataset.lng);
          var endCoordinates = this.dataset.end.split(",");
          var endLatitude = parseFloat(endCoordinates[0].trim());
          var endLongitude = parseFloat(endCoordinates[1].trim());

          var end = new google.maps.LatLng(endLatitude, endLongitude);
          var start = new google.maps.LatLng(startLatitude, startLongitude)

          calculateAndDisplayRoute(endLatitude, endLongitude, start);
      });
  });
}