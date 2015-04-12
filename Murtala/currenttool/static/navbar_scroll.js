$(window).scroll(
    {
        previousTop: 0
    }, 
    function () {
    var currentTop = $(window).scrollTop();
    if (currentTop < this.previousTop) {
        $(".sidebar em").text("Up"); /* optional for demo */
        $(".header").show();
    } else {
        $(".sidebar em").text("Down");
        $(".header").hide();
    }
    this.previousTop = currentTop;
});