$(window).scroll(function () {
    if ($(window).scrollTop() >= 30) {
    $('#header').css('background','#e9e8e6');
    $('#header').css('box-shadow', '0px 0px 25px 0 rgba(0, 0, 0, 0.08)');

    } 
    else {
    $('#header').css('background','transparent');
    $('#header').css({'-webkit-box-shadow' : 'none', '-moz-box-shadow' : 'none', 'box-shadow' : 'none'});

    }
 });

 window.onload = function () {
    jQuery('body').css({'overflow': 'auto', 'position': 'static'});
    window.scrollTo(0, 0);
  };