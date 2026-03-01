const nav = document.querySelector(".nav");
const toggle = document.querySelector(".menu-toggle");
const menu = document.querySelector("#primary-menu");

if (nav && toggle && menu) {
  const closeMenu = () => {
    nav.dataset.open = "false";
    toggle.setAttribute("aria-expanded", "false");
  };

  const openMenu = () => {
    nav.dataset.open = "true";
    toggle.setAttribute("aria-expanded", "true");
  };

  toggle.addEventListener("click", () => {
    const isOpen = nav.dataset.open === "true";
    if (isOpen) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  menu.querySelectorAll("a").forEach((link) => {
    link.addEventListener("click", () => {
      closeMenu();
    });
  });

  window.addEventListener("resize", () => {
    if (window.innerWidth >= 704) {
      closeMenu();
    }
  });

  window.addEventListener("keydown", (event) => {
    if (event.key === "Escape") {
      closeMenu();
      toggle.focus();
    }
  });

  closeMenu();
}
