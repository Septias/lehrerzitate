
function toggleview(elem){
	$.ajax({
		url: 'ajax/toggle_visibility/' + elem.getAttribute('quoteid'),
		success: function (data){
            console.log(data);
			if (data == 1){
				elem.innerHTML = '<i class="fas fa-eye"></i>';
            }
			else{
				elem.innerHTML = '<i class="fas fa-eye-slash"></i>';
			}
		}
	})
}
