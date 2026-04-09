console.log("Website Loaded");

// Example: Navbar scroll effect
window.addEventListener("scroll", function () {
    document.querySelector(".navbar").style.background = "#000";
});

const menuToggle = document.getElementById("menuToggle");
const navLinks = document.getElementById("navLinks");

menuToggle.addEventListener("click", () => {
    navLinks.classList.toggle("active");
}); 

window.addEventListener("load", () => {
    document.getElementById("loader").style.display = "none";
});