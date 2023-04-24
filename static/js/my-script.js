fetch('../data/stops.txt')
.then(response => response.text())
.then(data => {
// parse the CSV data using the csv-parser library
const csv = require('csv-parser');
const results = [];
csv({ delimiter: ',' })
  .fromString(data)
  .on('data', (row) => {
    results.push(row);
  })
  .on('end', () => {
    // save the parsed data to the busStops variable
    const busStops = results;
    console.log(busStops); // display the parsed data in the console
  });
})
.catch(error => console.error(error));

function initMap() {
  var myLatLng = {lat: -35.282265, lng: 149.128749};
  var map = new google.maps.Map(document.getElementById('map'), {
    zoom: 12,
    center: myLatLng,
    mapId: '61438499f9d434c2',
  });

// Create a marker for each bus stop and add an event listener
for (var i = 0; i < busStops.length; i++) {
    var busStop = busStops[i];

    // Create a marker with a custom icon
    var marker = new google.maps.Marker({
        position: {lat: busStop.stop_lat, lng: busStop.stop_log},
        map: map,
        icon: 'https://maps.google.com/mapfiles/kml/pal4/icon47.png'
    });

    // Add an event listener to display information about the bus stop when the marker is clicked
    marker.addListener('click', function() {
    var contentString = '<h3>' + busStop.name + '</h3>' +
                        '<p>' + busStop.address + '</p>' +
                        '<p>Routes: ' + busStop.routes.join(', ') + '</p>';

    var infowindow = new google.maps.InfoWindow({
      content: contentString
    });

    infowindow.open(map, marker);
    });
    }
}