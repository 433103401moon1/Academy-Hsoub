$(function () {
  // header
  $(window).scroll(function () {
    var scrollTop = $(this).scrollTop();
    var scrollThreshold = 250;

    if (scrollTop > scrollThreshold) {
      $("#header").css("background-color", "#fff").addClass("scrolled");
      $("#header button").css("color", "#16aeca");

      $("#header button.navbar-toggler").focus(function () {
        $(this).css("border-color", "#16aeca");
      });
      $("#header button.navbar-toggler").blur(function () {
        $(this).css("border-color", "transparent");
      });
    } else {
      $("#header").css("background-color", "unset").removeClass("scrolled");
      $("#header button").css("color", "#fff");

      $("#header button.navbar-toggler").focus(function () {
        $(this).css("border-color", "#fff");
      });
      $("#header button.navbar-toggler").blur(function () {
        $(this).css("border-color", "transparent");
      });
    }

    $("#header .nav-link").removeClass("active");
    if (scrollTop >= $("#contact-us").offset().top - 100) {
      $('a[href="#contact-us"]').addClass("active");
    } else if (scrollTop >= $("#statistics").offset().top - 100) {
      $('a[href="#statistics"]').addClass("active");
    } else if (scrollTop >= $("#our-business").offset().top - 100) {
      $('a[href="#our-business"]').addClass("active");
    } else if (scrollTop >= $("#company-services").offset().top - 100) {
      $('a[href="#company-services"]').addClass("active");
    }
  });

  $("#header .nav-link").click(function () {
    $("#header .nav-link").removeClass("active");
    $(this).addClass("active");
  });

  // company-services: card-text
  $("#company-services .card").hover(
    function () {
      var cardText = $(this).find(".card-text");
      var contentHeight = cardText.prop("scrollHeight");
      cardText.css("height", contentHeight);
    },
    function () {
      $(this).find(".card-text").css("height", 0);
    }
  );

  // our-business
  $("#our-business .projecte").click(function () {
    var imgSrc = $(this).find("img").attr("src");
    var imgAlt = $(this).find("img").attr("alt");
    $("#our-business-overlay img").attr("src", imgSrc);
    $("#our-business-overlay img").attr("alt", imgAlt);

    $("#our-business-overlay").css({
      width: "100%",
      height: "100vh",
      opacity: "1",
      top: "0",
    });

    $("#our-business-overlay .close").click(function () {
      $("#our-business-overlay").css({
        width: "0",
        height: "0",
        opacity: "0",
        top: "50%",
      });
    });
  });
// statistics : counter
function isScrolledIntoView(elem) {
  var rect = elem.getBoundingClientRect();
  return rect.top >= 0 && rect.bottom <= window.innerHeight;
}

var counterNumberStarted = false;

window.addEventListener("scroll", function () {
  var counter = document.querySelector(".counter");
  if (counter && !counterNumberStarted && isScrolledIntoView(counter)) {
      countTo(counter);
      counterNumberStarted = true;
  }
});

function countTo(element) {
  let target = +element.getAttribute('data-target');
  let count = 0, increment = Math.ceil(target / 100);

  let counterInterval = setInterval(function () {
      count += increment;
      element.innerText = count >= target ? target : count;
      if (count >= target) clearInterval(counterInterval);
  }, 30);
}


  // footer: current-year
  var currentYear = new Date().getFullYear();
  $("#footer #current-year").text(currentYear.toString());
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
