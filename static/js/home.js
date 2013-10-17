$(document).ready(function() {

	// On form submission
	$('#upload_form').submit(function() { 
		// Make ajax request
		$(this).ajaxSubmit({
			success: function(data, status_code, jqxhr) {
				
			}
		}); 

		return false; 
	});

});
