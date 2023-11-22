var lat;
var pos;
    function initMap() {
        map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: 13.736694 , lng:100.531658},
        zoom: 14
        });
    }
function goto_homepage(){
    window.location.href = "Homepage.html";
}
function click_mylocation(){
    document.getElementById("buttoncon1").style.color = "green";
    document.getElementById("buttoncon2").style.backgroundColor = "#FAFAFA";
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
        pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
        }; 
        map.setCenter(pos);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(pos.lat, pos.lng),
            map: map,
            title: 'ตำแหน่งของคุณ'
         }); 
        },function() {
        handleLocationError(true, infoWindow, map.getCenter()); 
        });
    }
  
}
function click_display(){
    var Ra = document.getElementById("input2").value;
    var antennasCircle = new google.maps.Circle({
        strokeColor: "Green",
        strokeOpacity: 0.8,
        strokeWeight: 2,
        fillColor: "#1ed760",
        fillOpacity: 0.35,
        map: map,
        center: {
          lat: pos.lat,
          lng: pos.lng
        },
        radius: Ra*1000
      });
      map.fitBounds(antennasCircle.getBounds());
      
}
function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition); {
        pos = {
        lat: position.coords.latitude,
        lng: position.coords.longitude,
        }; 
        map.setCenter(pos);
        var marker = new google.maps.Marker({
            position: new google.maps.LatLng(pos.lat, pos.lng),
            map: map,
            title: 'ตำแหน่งของคุณ'
            }); 
        }
    }
     else {
        alert("Geolocation is not supported by this browser.");
    }
}

function showPosition(position) {
    document.getElementById("id_location").value = position.coords.latitude + "," + position.coords.longitude;
}