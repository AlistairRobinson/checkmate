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
        loop: false,
        cursor: "_"
    });
    (function execute() { 
        typewriter.deleteAll()
        .pauseFor(1000)
        .typeString(getCode())
        .pauseFor(1000)
        .start();
        setTimeout(execute, 10000);
    })();
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