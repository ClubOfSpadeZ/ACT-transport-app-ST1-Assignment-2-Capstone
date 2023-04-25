var xhr = new XMLHttpRequest();
xhr.open('GET', 'static/data/stopList.json', true);
xhr.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    BusStop = JSON.parse(this.responseText);
    console.log(BusStop);
  }
};
xhr.send();

// for (let x in BusStop) {

//     var markerCHISHOLM = [];

//     BusStop[x].forEach(([position, title, Stop_ID], i) => {

//         var icon = {
//             url: 'static/assest/Bus_Pictogram.png',
//             scaledSize: new google.maps.Size(20, 20) // Change the size of icon here
//         };

//         // Create a marker with a custom icon
//         var markerCHISHOLM = new google.maps.Marker({
//           position,
//           map: map,
//           icon: icon,
//           optimized: true,
//         });

//         // Create a new info window for each marker
//         var BusInfoWindow = new google.maps.InfoWindow({
//             content: '<h3>' + title + '</h3>' +
//                      '<p>' + Stop_ID + '</p>' +
//                      '<p>Routes</p>'
//         });

//         markers.push(markerCHISHOLM);

//         // Open the infoWindow when the marker is clicked
//         markerCHISHOLM.addListener("click", function() {
//             BusInfoWindow.open(map, markerCHISHOLM);
//         });

//         // Close the infoWindow when the map is clicked outside of it
//         markerCHISHOLM.addListener('mouseout', function() {
//             BusInfoWindow.close();
//         });

//         markerCHISHOLM.setVisible(false);
//     });

// }


for (let x in BusStop) {
  var value = BusStop[x];
  console.log(BusStop);
}

console.log(BusStop);