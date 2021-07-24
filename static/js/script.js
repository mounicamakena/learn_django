$(document).ready(function () {
    $('#myTable').DataTable({
        ajax: {
            url: "/netflix_data",
            method: "GET",
            dataSrc: "",
        },
        columns: [
            { "data": "show_id" },
            { "data": "show_type" },
            { "data": "title" },
            { "data": "director" },
            { "data": "cast" },
            { "data": "country" },
            { "data": "date_added" },
            { "data": "release_year" },
            { "data": "rating" },
            { "data": "duration" },
            { "data": "listed_in" },
            { "data": "description" },
        ]
    })
});