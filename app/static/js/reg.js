const $form = document.getElementById('registrationform');

$(document).ready(function() {
    $form.addEventListener('submit', (event) => {
        event.preventDefault();
        $("button").toggleClass("is-loading");
        $("button").prop("disabled", true);
        var input = { email: $('#email').val() };
        setTimeout(complete, 2000);
        console.log(input);
        $.post({
            url: "/add", 
            data: JSON.stringify(input),
            headers: {
                "Content-Type": "application/json"
            },
            success: complete(),
            error: error()
        });
        $("button").toggleClass("is-loading");
        $("button").prop("disabled", false);
    });
});

function complete() {
    return function(result) {
        $('#registrationform').fadeOut(500, function() {
            $('#registrationform').replaceWith("<h1 class='title is-2 has-text-black'>Registration successful</h1>" +
            "<p>Your key is: </p><h4 class='title is-4 is-family-monospace'>" + result['key'] + "</h4>" + 
            "<p>Please save your key and keep it safe - you will not be able to access it later.</p>" + 
            "<p>Now check out our <a class='has-text-weight-semibold has-text-black' href='/docs'>documentation</a> to start registering user accounts.</p>");
            $('#registrationform').fadeIn(500);
        });
    }
}

function error() {
    return function(xhr, status, error) {
        if (xhr['status'] == 400) {
            $('#error').html("An API key for this email already exists");
        } else {
            $('#error').html("An unexpected error occured, please try again later");
        }
    }
}
