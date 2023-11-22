var lat;
var pos;
async function initMap() {
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
function click_otherlocation(){
    document.getElementById("buttoncon2").style.color = "green";
    document.getElementById("buttoncon1").style.backgroundColor = "#FAFAFA";
    var  marker = new google.maps.Marker({
        position: new google.maps.LatLng( 13.736694, 100.531658),
        map: map,
        title: 'ตำแหน่งที่คุณเลือก',
        draggable: true,
    }); 
     google.maps.event.addListener(marker, 'dragend', function(){
        console.log(marker.getPosition().lat());
        console.log(marker.getPosition().lng());
        pos = {
            lat: marker.getPosition().lat(),
            lng: marker.getPosition().lng(),
            }; 
        // pos.lat=marker.getPosition().lat();
        // pos.lng=marker.getPosition().lng();
        map.setCenter(pos);
    }); 
}
