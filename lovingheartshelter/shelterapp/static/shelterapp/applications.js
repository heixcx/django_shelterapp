// Jquery for operations to adoption application
$(function() {

	// Present the pop-up form for creating a new application
	$(".newapplication").click(function () {
		$.ajax({
			url: '/shelterapp/my/apply/',
			type: 'get',
			dataType: 'json',
			beforeSend: function () {
				$("#mymodal").modal("show"); 
			},
			success: function (data) {
				$("#mymodal .modal-content").html(data.html_form);
				
			}
		});
	});
	
	/* 
	Submit form inputs for a new applicationa and 
	update the applications list asynchronously
	*/
	$("#mymodal").on("submit", ".create-form", function () {
		var form = $(this); // Store attributes and values of html form element
		$.ajax({
			url: form.attr("action"), 
			data: form.serialize(), // Create URL encoded text string
			type: form.attr("method"), 
			dataType: 'json',
			success: function (data) { 
				if (data.form_is_valid) {
					$("#table tbody").html(data.html_application_list); // Replace the html table body
					$("#mymodal").modal("hide");
				}
				else { 
					$("#mymodal .modal-content").html(data.html_form); // Stay in the pop-up form
				}
			}
		});
		return false;
	});

	// Present the pop-up form for application detail infomation
	$(".dt-info").click(function () {
		var btn = $(this); // Store attributes of html button element
		$.ajax({
			url: btn.attr('view-url'),
			type: 'get',
			dataType: 'json',
			beforeSend: function () {
				$("#mymodal").modal("show");
			},
			success: function (data) {
				$("#mymodal .modal-content").html(data.html_form);
				
			}
		});
	});

	// Present the pop-up form for editting an application
	$(".dt-edit").click(function () {
		var btn = $(this); // Store attributes of html button element
		$.ajax({
			url: btn.attr('update-url'),
			type: 'get',
			dataType: 'json',
			beforeSend: function () {
				$("#mymodal").modal("show");
			},
			success: function (data) {
				$("#mymodal .modal-content").html(data.html_form);
				
			}
		});
	});

	/* 
	Edit an exist applicationa and 
	update the applications list asynchronously
	*/
		$("#mymodal").on("submit", ".update-form", function () {
		var form = $(this); // Store attributes and values of html form element
		$.ajax({
			url: form.attr("action"),
			data: form.serialize(), // Create URL encoded text string 
			type: form.attr("method"),
			dataType: 'json',
			success: function (data) {
				if (data.form_is_valid) {
					$("#table tbody").html(data.html_application_list);  // Replace the html table body
					$("#mymodal").modal("hide");
				}
				else {
					$("#mymodal .modal-content").html(data.html_form); // Stay in the pop-up form
				}
			}
		});
		return false;
	});
});