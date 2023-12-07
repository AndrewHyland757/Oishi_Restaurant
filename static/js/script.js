


const navbarBrand = document.querySelector(".navbar-brand")







if ( window.location.href === 'https://8000-andrewhylan-oishirestau-lo9lr6ujhg0.ws-eu106.gitpod.io/') {
    navbarBrand.classList.add("brand-home");}
else {
    navbarBrand.classList.add("brand");}




document.querySelectorAll(".nav-link").forEach((link) => {
    if ( window.location.href === 'https://8000-andrewhylan-oishirestau-lo9lr6ujhg0.ws-eu106.gitpod.io/') {
        link.classList.add("nav-link-color-home");}
    else {
        link.classList.add("nav-link-color");}
    } 
);



/* adds the active class to the navigation link of current displayed page */
document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === "window.location.href") {
        link.parentElement.classList.add("active");
        link.setAttribute("aria-current", "page");
    }
});






/* function to remove an element, used on burger icon in nav-bar */
function remove(element) {
var element = element;
element.remove();
}




/* adds the active class to the navigation link of current displayed page */
document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === "window.location.href") {
        link.parentElement.classList.add("active");
        link.setAttribute("aria-current", "page");
    }
});







