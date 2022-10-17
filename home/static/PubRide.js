// To show calender
document.querySelector(".calenderIcon").addEventListener("click", function(){
    setDatepicker(this);
});

function setDatepicker(_this) {

/* Get the parent class name so we 
  can show date picker */
let className = $(_this).parent()
  .parent().parent().attr('class');

// Remove space and add '.'
let removeSpace = className.replace(' ', '.');

// jQuery class selector
$("." + removeSpace).datetimepicker({
  format: "mm/dd/yyyy",

  // Positioning where the calendar is placed
  orientation: "bottom auto",
  // Calendar closes when cursor is 
  // clicked outside the calendar
  autoclose: true,
  showOnFocus: "false"
});
}

// To reset the form on refreshing the page
function resetting(){
  document.form.reset();
}


// for time

  //   $(function () {
  //     $('#text-d618').datetimepicker();
  // });

// for taking no. of passengers

$(document).on('click', '.number-spinner .input-group-prepend', function () {    
	var btn = $(this),
		oldValue = btn.closest('.number-spinner').find('input').val().trim() || 0,
		newVal = 0;
	
	if (btn.attr('data-dir') == 'up') {
		newVal = parseInt(oldValue) + 1;
	} else {
		if (oldValue > 0) {
			newVal = parseInt(oldValue) - 1;
		} else {
			newVal = 0;
		}
	}
	btn.closest('.number-spinner').find('input').val(newVal);
});
