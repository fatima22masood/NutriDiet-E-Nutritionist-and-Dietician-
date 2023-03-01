//preloader js
// $(document).ready(function(){
// 	$('div#loading').removeAttr('id');
// });
var preloader = document.getElementById("loading");
// window.addEventListener('load', function(){
// 	preloader.style.display = 'none';
// 	})

function myFunction() {
  preloader.style.display = "none";
}

//preloadfer js ending

// initialize swiper js

const swiper = new Swiper(".swiper", {
  loop: true,
  // If we need pagination
  pagination: {
    el: ".swiper-pagination",
  },
  // Navigation arrows
  navigation: {
    nextEl: ".swiper-button-next",
    prevEl: ".swiper-button-prev",
  },
});

// FAQ js
let accordion = document.querySelectorAll(
  ".faq .accordion-container .accordion"
);

accordion.forEach((acco) => {
  acco.onclick = () => {
    accordion.forEach((dion) => dion.classList.remove("active"));
    acco.classList.toggle("active");
  };
});

document.querySelector(".load-more .btn").onclick = () => {
  document.querySelectorAll(".contact .box-container .hide").forEach((show) => {
    show.style.display = "block";
  });
  document.querySelector(".load-more .btn").style.display = "none";
};
