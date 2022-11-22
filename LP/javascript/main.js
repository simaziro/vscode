
/******************スライダー******************/ 

$(document).ready(function(){
  $('.slider').slick({
  arrows: true, // 前・次のボタンを表示する
  dots: true, // ドットナビゲーションを表示する
  autoplay: true,
  loop: true,
  speed: 1000, // スライドさせるスピード（ミリ秒）
  slidesToShow: 3, // 表示させるスライド数
  centerMode: true, // slidesToShowが奇数のとき、現在のスライドを中央に表示する
  centerPadding: '0px',
  variableWidth: true, // スライド幅の自動計算を無効化
  autoplaySpeed:800,
  centerMode: true,
  swipe: true,
  responsive: [{
      breakpoint: 2,
      settings: {
        slidesToShow: 1,
        centerPadding: 0,
        fade: true
      }
    }]
  });});


/******************イベントカード ******************/ 

$(document).ready(function(){
var zindex = 10;

$("li.card7").click(function(e){
  e.preventDefault();

  var isShowing = false;

  if ($(this).hasClass("show")) {
    isShowing = true
  }

  if ($("ul.cards7").hasClass("showing")) {
    $("li.card7.show")
      .removeClass("show");

    if (isShowing) {
      $("ul.cards7")
        .removeClass("showing");
    } else {
      $(this)
        .css({zIndex: zindex})
        .addClass("show");

    }

    zindex++;

  } else {
    // no cards in view
    $("ul.cards7")
      .addClass("showing");
    $(this)
      .css({zIndex:zindex})
      .addClass("show");
    zindex++;
  }
  
});
});

/******************イベントカード スワイパー******************/ 

const swiper = new Swiper('.swiper', {
// Optional parameters
direction: 'horizontal',
loop: true,
centerSlide:true,
speed:1000,
effect: 'slider',
cardsEffect: {
  slideShadows:false,
},

// If we need pagination
pagination: {
  el: '.swiper-pagination',
  navigation:true,
  with:8,
  type:ProgressEvent,
},


// Navigation arrows
navigation: {
  nextEl: '.swiper-button-next',
  prevEl: '.swiper-button-prev',
},

// And if we need scrollbar
scrollbar: {
  el: '.swiper-scrollbar',
  hide:true,
},
});

/******************給料******************/ 

