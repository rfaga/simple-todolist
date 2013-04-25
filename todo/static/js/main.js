$(function() {
	$('body').on('click', '.modal-loader', function(event){
		event.preventDefault();
		var url = $(this).attr('data-url');
		$('#modal-todo').load(url);
		$('#modal-todo').modal('show');
	});
	
	
	
	$('#modal-todo').on('click', '.modal-submit', function(event){
		event.preventDefault();
		var url = $(this).attr('data-url');
		var modal = $(this).parents('.modal');
		$.ajax({
			type: "POST",
			url: url,
			data: $('form.task-form').serializeArray(),
			success: function(msg){
				if (msg) {
					modal.html(msg);
				} else {
					$('#tasks-list tbody').load(list_url);
					modal.modal('hide');
				};
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				modal.html(XMLHttpRequest.responseText);
			}
		});		
	});
	
	
	$('#modal-todo').on('click', '.modal-remove', function(event){
		event.preventDefault();
		var url = $(this).attr('data-url');
		var modal = $(this).parents('.modal');
		$.ajax({
			type: "GET",
			url: url,
			success: function(msg){
				if (msg) {
					modal.html(msg);
				} else {
					$('#tasks-list tbody').load(list_url);
					modal.modal('hide');
				};
			},
			error: function(XMLHttpRequest, textStatus, errorThrown) {
				modal.html(XMLHttpRequest.responseText);
			}
		});						
	});
});


