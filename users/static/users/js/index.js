function clickBtn() {
	$(".block").toggle();
}

$(document).ready(function() {
	$("#slider").slick({
		dots: false,
		prevArrow: '<div class="arrow-prev"><i class="fas fa-arrow-left"></i></div>',
		nextArrow: '<div class="arrow-next"><i class="fas fa-arrow-right"></i></div>',
		infinite: true,
		slidesToShow: 1,
		slidesToScroll: 1
	});
});
