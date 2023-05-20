// JavaScript code for loader

// Wait for the DOM to be fully loaded
function myFunction() {
  // Hide the loader element
  var loader = document.getElementById("loading");
  loader.style.display = "none";
}

//loader js ending


// JavaScript code to initialize Swiper

// Wait for the DOM to be fully loaded
document.addEventListener("DOMContentLoaded", function () {
  // Initialize Swiper
  var swiper = new Swiper('.reviews-slider', {
    // Set the desired configuration options for the slider
    loop: true,
    navigation: {
      nextEl: '.swiper-button-next',
      prevEl: '.swiper-button-prev',
    },
  });
});


// JavaScript code for FAQ section
document.addEventListener("DOMContentLoaded", function () {
  var accordions = document.querySelectorAll(".faq .accordion");

  accordions.forEach(function (accordion) {
    accordion.addEventListener("click", function () {
      var isActive = this.classList.contains("active");

      accordions.forEach(function (otherAccordion) {
        otherAccordion.classList.remove("active");
        var accordionContent = otherAccordion.querySelector(".accordion-content");
        accordionContent.style.maxHeight = null;
      });

      if (!isActive) {
        this.classList.add("active");
        var accordionContent = this.querySelector(".accordion-content");
        accordionContent.style.maxHeight = accordionContent.scrollHeight + "px";
      }
    });
  });
});
