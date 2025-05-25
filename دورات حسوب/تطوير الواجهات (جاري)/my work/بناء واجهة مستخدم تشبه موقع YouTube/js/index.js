$(function () {
    // top-menu
    $("#top-menu .nav-link").click(function () {
        $("#top-menu .nav-link").removeClass("active");
        $(this).addClass("active");
    });
    $("#icon-search").click(function () {
        $("#input-search-fluid").toggleClass("active");
    });

    // side-menu
    $("#icon-side-menu, #side-menu #background-side-menu").click(function () {
        $("#side-menu #background-side-menu, #side-menu ul").toggleClass("active");
    });

    // video-remove
    $(".card .video-remove").click(function () {
        $(this).parent().parent().parent().css("display", "none");
    });

    // filter-items
    $("#search-filter").click(function () {
        $("#filter-items").toggleClass("active");
    });

    function handleCheckboxChange(checkboxName) {
        $('input[name="' + checkboxName + '"]').change(function () {
            $('input[name="' + checkboxName + '"]').not(this).prop('checked', false).parent().removeClass('selected');
            if ($(this).is(':checked')) {
                $(this).parent().addClass('selected');
            } else {
                $(this).parent().removeClass('selected');
            }
        });
    }

    handleCheckboxChange("download-date");
    handleCheckboxChange("type");
    handleCheckboxChange("sort-by");
    handleCheckboxChange("duration");


    // channel-page
    $("#channel-page .nav-link").click(function () {
        $("#channel-page .nav-link").removeClass("active");
        $(this).addClass("active");
    });

    // watch-page
    $("#watch-page .show-more").click(function () {
        $("#watch-page .card-body .card-text").toggleClass("active");
        $("#watch-page .show-more").removeClass("d-none");
        $(this).addClass("d-none");
    });

    $("#watch-page .sub-comments").click(function () {
        $(this).closest('.card').find('.sub-comment').toggleClass("d-none");
    });

});
