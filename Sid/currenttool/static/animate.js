var main = function() {
	$('.pull-left').click(function() {
		$('.nav').animate({
			down: '0px'
		}, 200);
	});
};

$(document).ready(main);