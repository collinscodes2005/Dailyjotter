const hamburgerMenuButton = document.getElementById("hamburger-menu-button");
const navigation = document.getElementById("navigation");

hamburgerMenuButton.addEventListener("click", function() {
  navigation.classList.toggle("show");
});
