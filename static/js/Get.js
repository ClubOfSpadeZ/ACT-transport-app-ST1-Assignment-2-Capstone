var BusRoute;

var xhr = new XMLHttpRequest();
xhr.open('GET', 'C:\Users\FireH\PycharmProjects\ACT-transport-app-ST1-Assignment-2-Capstone\static\data\Bus_Routes.xml', true);
xhr.onreadystatechange = function() {
  if (this.readyState === 4 && this.status === 200) {
    BusRoute = JSON.parse(this.responseText);
    console.log(BusRoute);
  }
};
xhr.send();

// Assume xmlData is the XML string to be processed
const parser = new DOMParser();
const xmlDoc = parser.parseFromString(BusRoute, "text/xml");

const rows = xmlDoc.getElementsByTagName("row");
const nestedArray = [];

for (let i = 0; i < rows.length; i++) {
  const row = rows[i];
  const attributes = row.attributes;
  const rowData = {};

  for (let j = 0; j < attributes.length; j++) {
    const attribute = attributes[j];
    rowData[attribute.nodeName] = attribute.nodeValue;
  }

  const children = row.children;
  for (let j = 0; j < children.length; j++) {
    const child = children[j];
    rowData[child.nodeName] = child.textContent;
  }

  nestedArray.push(rowData);
}

console.log(nestedArray);