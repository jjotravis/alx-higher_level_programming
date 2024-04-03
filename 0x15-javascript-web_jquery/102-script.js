$('document').ready(function () {
    const url = 'https://www.fourtonfish.com/hellosalut/?'
    $('INPUT#btn_translate').click(function () {
        // var languange = $('INPUT#language_code').val();
        $.get(url + $.param({ lang: $('INPUT#language_code').val() }), function(response) {
            $('DIV#hello').html(response.hello);
        });
    });
});