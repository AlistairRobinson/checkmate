$(document).ready(function() {
    $(".navbar-burger").click(function() {
        $(".navbar-burger").toggleClass("is-active");
        $(".navbar-menu").toggleClass("is-active");
    });

    typewriter();
});

function typewriter() {
    var showcase = document.getElementById('showcase');
    var typewriter = new Typewriter(showcase, { 
        loop: true,
        cursor: "_"
    });
    console.log("hello");
    typewriter.typeString('Hello World!')
        .pauseFor(2500)
        .deleteAll()
        .pauseFor(2500)
        .start();
}
