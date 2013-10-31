$(document).ready(function() {

	xlp = new XLPlot("map-canvas");

	// On form submission
	$('#upload_form').submit(function() { 
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
