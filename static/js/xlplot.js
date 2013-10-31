function XLPlot(map_eid) {
	var mapOptions = {
		zoom: 3, 
		center: new google.maps.LatLng(37.774546, -122.433523),
	};

	if(map_eid == undefined || map_eid == "") {
		throw "Invalid values for map id";
	} else {
		this.map = new google.maps.Map(document.getElementById(map_eid),
				mapOptions);
	}
}

XLPlot.prototype.addMarkers = function(data) {
	var len = data.length;
	for(i = 0; i < len; i++) {
		var marker = new google.maps.Marker({    
      position: new google.maps.LatLng(data[i].lat, data[i].lng),
      map: this.map
    });  
	}
}
