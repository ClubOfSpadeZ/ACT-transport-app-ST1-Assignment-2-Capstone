var BusStop;
var map;

var xhr = new XMLHttpRequest();
xhr.open('GET', 'static/data/stopList.json', true);
xhr.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    BusStop = JSON.parse(this.responseText);
    console.log(BusStop["CHISHOLM"]);
  }
};
xhr.send();

function initMap() {

    var myLatLng = {lat: -35.282265, lng: 149.128749};

    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 12,
        center: myLatLng,
        mapId: '61438499f9d434c2',
        });

    var markers = [];

    for (let x in BusStop) {

        var markersName = "marker" + x.replace(/[^\w]+/g, '');
        window[markersName] = [];
    
        BusStop[x].forEach(([position, title, Stop_ID], i) => {

            var icon = {
                url: 'static/assest/Bus_Pictogram.png',
                scaledSize: new google.maps.Size(20, 20), // Change the size of icon here
            };
    
            // Create a marker with a custom icon
            window[markersName] = new google.maps.Marker({
              position,
              map: map,
              title: Stop_ID + ':\t' + title,
              icon: icon,
              optimized: true,
            });
    
            markers.push(window[markersName]);

            // Create a new info window for each marker
            var BusInfoWindow = new google.maps.InfoWindow({
                content: '<h3>' + title + '</h3>' +
                         '<p>' + Stop_ID + '</p>' +
                         '<p>' + JSON.stringify(position) + '</p>',
                pixelOffset: new google.maps.Size(0, -10)
            });
    
            // Open the infoWindow when the marker is clicked
            window[markersName].addListener("click", function() {
                BusInfoWindow.setContent('<h3>' + title + '</h3>' +
                                          '<p>' + Stop_ID + '</p>' +
                                          '<p>' + JSON.stringify(position) + '</p>');
                BusInfoWindow.setPosition(position);
                BusInfoWindow.open(map);
              });
    
            // Close the infoWindow when the map is clicked outside of it
            window[markersName].addListener('mouseout', function() {
                BusInfoWindow.close();
            });
    
            window[markersName].setVisible(false);
        });
    }

    google.maps.event.addListener(map, 'idle', function() {
        var bounds = map.getBounds();
        var zoom = map.getZoom();
    //            console.log('RUN')
            for (var i = 0; i < markers.length; i++) {
                window[markersName] = markers[i];
                if (bounds.contains(window[markersName].getPosition())) {
                    window[markersName].setVisible(zoom >= 15);
                } else {
                    window[markersName].setVisible(false);
                }
            }
     });
}

window.initMap = initMap;