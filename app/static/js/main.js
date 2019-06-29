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
    typewriter.typeString(getCode())
        .pauseFor(1000)
        .deleteAll()
        .pauseFor(1000)
        .start();
}

function getCode() {
    var example = "";
    $.post({
        url: "/showcase", 
        datatype: "json",
        async: false,
        success: function(result) {
            example = result['w1'] + " " + result['w2'] + " "
                    + result['w3'] + " " + result['pin'];
        }
    });
    return example;
}