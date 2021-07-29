$(document).ready(function () {
    $('#myTable').DataTable({
        ajax: {
            url: "/planet",
            method: "GET",
            dataSrc: "",
        },
        columns: [
            { "data": "image_name" },
            { "data": "tags" },

        ]
    })
});