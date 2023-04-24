function readXml(xmlFile, stopNum) {

    var xmlDoc;

    if(typeof window.DOMParser != "undefined") {
        xmlhttp=new XMLHttpRequest();
        xmlhttp.open("GET",xmlFile,false);
        if (xmlhttp.overrideMimeType){
            xmlhttp.overrideMimeType('text/xml');
        }
        xmlhttp.send();
        xmlDoc=xmlhttp.responseXML;
    }
    else{
        xmlDoc = new ActiveXObject("Microsoft.XMLDOM");
        xmlDoc.async="false";
        xmlDoc.load(xmlFile);
    }
    var tagObj = xmlDoc.getElementsByTagName("row");
    var stopID = tagObj[stopNum].getElementsByTagName("stop_id")[0].childNodes[0].nodeValue;
    var stopLat = tagObj[stopNum].getElementsByTagName("stop_latitude")[0].childNodes[0].nodeValue;
    var stopLon = tagObj[stopNum].getElementsByTagName("stop_longitude")[0].childNodes[0].nodeValue;
    return [stopID, stopLat, stopLon]
    }

document.getElementById("demo").innerHTML = readXml('/static/data/Bus_Stops.xml', 5)[0];