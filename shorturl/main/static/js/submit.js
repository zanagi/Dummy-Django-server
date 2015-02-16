var url = window.location.href;

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
	var data = $("#url").val();
	if(url.length > 0){
		$.ajax({
			type: "POST",
			url: url,
			data: data,
			contentType: "application/x-www-form-urlencoded",
			success: function(d){
				var linkobj = $("#newlink")
				var newurl = url + "/" + d
				linkobj.text(newurl);
				linkobj.attr("href", newurl);
				console.log("id: " + d);
			},
		});
	}
}

