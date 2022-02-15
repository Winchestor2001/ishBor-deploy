$(document).ready(function () {
  $(".carousel").owlCarousel({
    margin: 20,
    loop: true,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    speed: 8000,
    responsiveClass: true,
    responsive: {
      0: {
        items: 1,

      },
      600: {
        items: 1,

      },
      1000: {
        items: 2,

      }
    }
  });
  $('.caseStudyCarusel').owlCarousel({
    loop: true,
    // margin: 5,
    autoplay: true,
    autoplayTimeout: 3000,
    autoplayHoverPause: true,
    speed: 8000,
    responsiveClass: true,
    responsive: {
      0: {
        items: 2
      },
      600: {
        items: 3
      },
      1000: {
        items: 6
      }
    }
  })
  $('.owl-carousel').owlCarousel({
    loop: true,
    // margin: 5,
    autoplay: true,
    animateOut: 'fadeOut',
    autoplayTimeout: 4000,
    // autoplayHoverPause: true,
    speed: 8000,
    responsiveClass: true,
    items: 1,
  })

  let scrol = $(".scrolTop").hide();
  // $(".scrolTop").hide();
  console.log(scrol)
  $(window).scroll(function () {

    let scroltop = $("html").scrollTop();
    console.log(scroltop);
    if (scroltop >= 200) {
      scrol.show()
    }
    else {
      scrol.hide()
    }

  });
  $(".scrolTop").click(function () {
    $("html").animate({
      scrollTop: "0"

    }, 100)
  })
})





const menuBtn = document.querySelector('.menu-btn');
let menuOpen = false;
menuBtn.addEventListener('click', () => {
  if (!menuOpen) {
    menuBtn.classList.add('open');
    menuOpen = true
  }
  else {
    menuBtn.classList.remove('open');
    menuOpen = false
  }
})
//let scrollTop=document.getElementById('scrollTop');
//window.addEventListener('scroll',()=>{
// if(window.pageYOffset>300){
// console.log(window.pageYOffset)
//    scrollTop.style.display='block';
// }else{
//    scrollTop.style.display='none';
// }
//})
