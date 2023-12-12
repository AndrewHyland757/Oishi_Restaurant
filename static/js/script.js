

/*
const navbarBrand = document.querySelector(".navbar-brand")

if (location.pathname === '/' || location.pathname === '/#reservation/' ) {
    navbarBrand.classList.add("brand-home");}

else {
    navbarBrand.classList.add("brand");}


document.querySelectorAll(".nav-link").forEach((link) => {
    if (location.pathname === '/') {
        link.classList.add("nav-link-color-home");}
    else {
        link.classList.add("nav-link-color");}
    } 
);

*/

document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === window.location.href) {
        link.classList.add("active-link");
        link.setAttribute("aria-current", "page");
    }
});



function remove(element) {
var element = element;
element.remove();
}











