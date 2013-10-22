function initialize() {

	var mapOptions = {
		zoom: 3, 
		center: new google.maps.LatLng(37.774546, -122.433523),
	};

	map = new google.maps.Map(document.getElementById('map-canvas'),
			mapOptions);

	addMarkers(map, window.coord_data);
	//addHeatmap(map);

}

function addMarkers(map, data) {
	var len = data.length;
	for(i = 0; i < len; i++) {
		var marker = new google.maps.Marker({    
      position: new google.maps.LatLng(coord_data[i].lat, coord_data[i].lng),
      map: map    
    });  
	}
}

function addHeatmap(map) {
	var data = [];
	var len = window.coord_data.length;
	for(i = 0; i < len; i++) {
		data.push(new google.maps.LatLng(coord_data[i].lat, coord_data[i].lng));
	}

	var pointArray = new google.maps.MVCArray(data);

	heatmap = new google.maps.visualization.HeatmapLayer({
		data: pointArray
	});

  var gradient = [
    'rgba(0, 255, 255, 0)',
    'rgba(0, 255, 255, 1)',
    'rgba(0, 191, 255, 1)',
    'rgba(0, 127, 255, 1)',
    'rgba(0, 63, 255, 1)',
    'rgba(0, 0, 255, 1)',
    'rgba(0, 0, 223, 1)',
    'rgba(0, 0, 191, 1)',
    'rgba(0, 0, 159, 1)',
    'rgba(0, 0, 127, 1)',
    'rgba(63, 0, 91, 1)',
    'rgba(127, 0, 63, 1)',
    'rgba(191, 0, 31, 1)',
    'rgba(255, 0, 0, 1)'
  ]

  heatmap.setOptions({
    gradient: heatmap.get('gradient') ? null : gradient
  });

	heatmap.setMap(map);
}

//google.maps.event.addDomListener(window, 'load', initialize);
