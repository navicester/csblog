$(document).ready(function () {
    $("#id_tags").autocomplete({
        // source: "/ajax/tag/autocomplete/"
        source: function (request, response) {
            $.ajax({
                url: "/ajax/tag/autocomplete/",
                data: { q:$("input#id_tags").val() },
                success: function (data) {
                    response(JSON.parse(data))
                },
                error: function () {
                    response([]);
                }
            });
        },
    });    

});    

// https://stackoverflow.com/questions/12370614/jquery-ui-autocomplete-with-json-from-url