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

XLPlot.prototype.getMapList = function() {
	
};


$(document).ready(function() {
	xlp = new XLPlot("map-canvas");

	// On form submission
	$('#upload_form').submit(function(e) {
		e.preventDefault();

		// Make ajax request
		$(this).ajaxSubmit({
			success: function(data, status_code, jqxhr) {
				xlp.addMarkers(data["locations"]);
				console.log("added markers");
			}
		}); 

		return false;
	});
});
