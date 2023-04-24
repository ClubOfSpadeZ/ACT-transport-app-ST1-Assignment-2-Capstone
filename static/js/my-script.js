var BusStop;

var xhr = new XMLHttpRequest();
xhr.open('GET', 'static/data/stopList.json', true);
xhr.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    BusStop = JSON.parse(this.responseText);
    console.log(BusStop);
  }
};
xhr.send();

function initMap() {

    var myLatLng = {lat: -35.282265, lng: 149.128749};
    console.log(BusStop);

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: myLatLng,
        mapId: '61438499f9d434c2',
        });

    var markers = [];

    var markersCHISHOLM = []

    BusStop["CHISHOLM"].forEach(([position, title, Stop_ID], i) => {

        var icon = {
            url: 'static/assest/Bus_Pictogram.png',
            scaledSize: new google.maps.Size(20, 20) // Change the size of icon here
        };

        // Create a marker with a custom icon
        var marker = new google.maps.Marker({
          position,
          map: map,
          icon: icon,
          optimized: true,
        });

        // Create a new info window for each marker
        var BusInfoWindow = new google.maps.InfoWindow({
            content: '<h3>' + title + '</h3>' +
                     '<p>' + Stop_ID + '</p>' +
                     '<p>Routes</p>'
        });

        markers.push(marker);

        // Open the infoWindow when the marker is clicked
        marker.addListener("click", function() {
            BusInfoWindow.open(map, marker);
        });

        // Close the infoWindow when the map is clicked outside of it
        marker.addListener('mouseout', function() {
            BusInfoWindow.close();
        });

        marker.setVisible(false);
    });


    google.maps.event.addListener(map, 'idle', function() {
    var bounds = map.getBounds();
    var zoom = map.getZoom();
//            console.log('RUN')
        for (var i = 0; i < markers.length; i++) {
            var marker = markers[i];
            if (bounds.contains(marker.getPosition())) {
            marker.setVisible(zoom >= 15);
            } else {
            marker.setVisible(false);
            }
        }
    });
}

window.initMap = initMap;