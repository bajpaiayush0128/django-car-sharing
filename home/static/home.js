// To show calender
// document.querySelector(".calenderIcon").addEventListener("click", function () {
//   setDatepicker(this);
// });

function setDatepicker(_this) {
  
  let className = $(_this).parent().parent().parent().attr("class");

  // Remove space and add '.'
  let removeSpace = className.replace(" ", ".");

  // jQuery class selector
  $("." + removeSpace).datepicker({
    format: "dd/mm/yyyy",

    // Positioning where the calendar is placed
    orientation: "bottom auto",
    // Calendar closes when cursor is
    // clicked outside the calendar
    autoclose: true,
    showOnFocus: "false",
  });
}

// for taking no. of passengers

$(document).on("click", ".number-spinner .input-group-prepend", function () {
  var btn = $(this),
    oldValue = btn.closest(".number-spinner").find("input").val().trim() || 0,
    newVal = 0;

  if (btn.attr("data-dir") == "up") {
    newVal = parseInt(oldValue) + 1;
  } else {
    if (oldValue > 0) {
      newVal = parseInt(oldValue) - 1;
    } else {
      newVal = 0;
    }
  }
  btn.closest(".number-spinner").find("input").val(newVal);
});

// Back-to-top start
function toTop() {
  window.scrollTo(0, 0);
}

$(window).scroll(() => {
  const scroll = $(window).scrollTop();

  if (scroll >= 150) {
    $(".bttBtn").addClass("active");
  } else {
    $(".bttBtn").removeClass("active");
  }
});
// Back-to-top ends
