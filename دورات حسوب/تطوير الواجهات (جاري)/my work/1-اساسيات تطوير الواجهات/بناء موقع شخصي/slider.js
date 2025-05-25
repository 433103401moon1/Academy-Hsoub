// لا يوجد اي تاثر لهذا الرمز في اسم المتغير $ فقط تم استخدامه للدلاله على ان هذا المتغير يرجع قيمة بواسطه جيكويري
var $links = $('.itemLinks');

$links.click(function (e) {
    // console.log(e)
    $links.removeClass('active');
    var clickedLink = e.target;
    clickedLink = $(clickedLink);
    var position = clickedLink.attr('data-pos');
    var translateValue = 'translateX('+ position * 20 +'%)'
    $('#wrapper').css({
        transform: translateValue
    });

    clickedLink.addClass('active');
});

$($links[0]).addClass('active');

