
/* Applies the active class to the link of the current page */

document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === window.location.href) {
        link.classList.add("active-link");
        link.setAttribute("aria-current", "page");
    }
});


/* Removes an element after being clicked - used on burger menu in nav bar */

function remove(elem) {
var element = elem;
element.remove();
}











