$(function () {
  // header: product-lable-text
  updateFontSize();

  $(window).on("resize", function () {
    updateFontSize();
  });

  function updateFontSize() {
    var productLabel = $("#header .card img.product-lable");
    var productLabelText = $("#header .card .product-lable-text");
    var labelWidth = productLabel.width();
    var fontSize = labelWidth * 0.01;
    productLabelText.css("font-size", fontSize + "rem");
  }

  // contact-us: video-play
  $("#video-show #video-play").click(function () {
    var video = $("#video-show video")[0];
    if (video.paused) {
      video.play();
      $(this).find("i").removeClass("fa-video").addClass("fa-pause");
      $(this).find("div").text("إيقاف الفيديو");
    } else {
      video.pause();
      $(this).find("i").removeClass("fa-pause").addClass("fa-video");
      $(this).find("div").text("مشاهدة الفيديو");
    }
  });

  // footer: current-year
  var currentYear = new Date().getFullYear();
  $('#footer #current-year').text(currentYear.toString());
});

(() => {
  "use strict";

  // Fetch all the forms we want to apply custom Bootstrap validation styles to
  const forms = document.querySelectorAll(".needs-validation");

  // Loop over them and prevent submission
  Array.from(forms).forEach((form) => {
    form.addEventListener(
      "submit",
      (event) => {
        if (!form.checkValidity()) {
          event.preventDefault();
          event.stopPropagation();
        }
        form.classList.add("was-validated");
      },
      false
    );
  });
})();
