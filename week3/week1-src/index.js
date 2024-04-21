let menuIcon = document.querySelector("#menu-icon");
let menuContainer = document.querySelector("#menu-container");

function showMenu() {
  if (menuIcon && menuContainer) {
    menuIcon.style.display = "none";
    menuContainer.style.display = "block";
  }
}

function closeMenu() {
  if (menuIcon && menuContainer) {
    menuIcon.style.display = "block";
    menuContainer.style.display = "none";
  }
}
