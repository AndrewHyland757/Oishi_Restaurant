


const navbarBrand = document.querySelector(".navbar-brand")

if (location.pathname === '/') {
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


document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === window.location.href) {
        link.classList.add("active-link");
        link.setAttribute("aria-current", "page");
    }
});









/*
$(function(){
    var current = location.pathname;
    $('#nav a').each(function(){
        var $this = $(this);
        // if the current path is like this link, make it active
        if($this.attr('href').indexOf(current) !== -1){
            $this.addClass('active-link');
        }
    })
})

*/

/* adds the active class to the navigation link of current displayed page */
/*
document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === "window.location.href") {
        link.Element.classList.add("active-link");
        link.setAttribute("aria-current", "page");
    }
});

*/

/* function to remove an element, used on burger icon in nav-bar */
function remove(element) {
var element = element;
element.remove();
}











