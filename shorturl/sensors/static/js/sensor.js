/* Setup AJAX to handle CORS with Django */
$(document).ready(function() {
	setupAjax();

	/* Setup AJAX to handle CORS with Django */
	function setupAjax(){
		/* Handling CSRF */
		var csrftoken = getCookie('csrftoken');
		
		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});
		
		function csrfSafeMethod(method) {
			return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
		}
		
		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}
	}
});

function post(){
	var sensor = $("#sensor").val();
	var value = $("#value").val();
	var url = window.location.href;
	
	if(sensor && $.isNumeric(value)){
		$.ajax({
			type: "POST",
			url: url,
			data: {"sensor":sensor, "value":value},
			contentType: "application/x-www-form-urlencoded",
			success: handleResponse,
		});
	} else {
		alert("Error! Missing sensor name or value, value must also be numeric");
	}
}

function handleResponse(d) {
	$("#info").html("Sensor added!");
	
	window.setTimeout(function(){
		$("#info").html("Info:");
	}, 1000);
}
