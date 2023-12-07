


  function remove(el) {
    var element = el;
    element.remove();
  }
  

  

  document.querySelectorAll(".nav-link").forEach((link) => {
    if (link.href === window.location.href) {
        link.parentElement.classList.add("active");
        link.setAttribute("aria-current", "page");
    }
});


document.querySelectorAll(".nav-link").forEach((link) => {
    if (window.location.href === "home") {
        link.classList.add("nav-link-color-home");}
    else {
        link.classList.add("nav-link-color");}
    }
    
);





