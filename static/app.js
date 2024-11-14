// Hamburger Menu Toggling Function

const menuBtn = document.querySelector(".mobile_menu");
const menuBox = document.querySelector(".mobile_links_popup");

menuBtn?.addEventListener("click", () => {
  menuBox.classList.toggle("active");
});

// Initializing Swiper JS
var swiper = new Swiper(".mySwiper", {
  spaceBetween: 40,
  pagination: {
    el: ".swiper-pagination",
    clickable: true,
  },
  grabCursor: true,
  autoplay: {
    delay: 2500,
    disableOnInteraction: false,
  },
});

// Initializing Locomotive Scroll
(function () {
  const locomotiveScroll = new LocomotiveScroll();
})();

// Faq Toggling Function
const faqCards = document.querySelectorAll(".faq_card");

faqCards.forEach((item) => {
  item.addEventListener("click", () => {
    faqCards.forEach((item) => item.classList.remove("active"));
    item.classList.add("active");
  });
});

// Step Cards Toggling Feature
document.addEventListener("DOMContentLoaded", () => {
  const stepCards = document.querySelectorAll(".step_card");

  stepCards.forEach(function (stepCard) {
    stepCard.addEventListener("click", function () {
      const targetIndex = this.getAttribute("data-target");
      const stepImages = document.querySelectorAll(".step_image");

      stepCards.forEach(function (card) {
        card.classList.remove("active");
      });
      this.classList.add("active");

      stepImages.forEach(function (image) {
        const imageIndex = image.getAttribute("data-index");
        if (imageIndex === targetIndex) {
          image.classList.add("active");
        } else {
          image.classList.remove("active");
        }
      });
    });
  });
});

// Navbar Active Toggle Function
const navbar = document.querySelector(".navbar");

window.addEventListener("scroll", function () {
  if (window.scrollY > 500) {
    navbar.classList.add("active");
  } else {
    navbar.classList.remove("active");
  }
});
