function check(v="You're code is bootiful") {
  // A general check that can be inserted anywhere
  console.log(v)
}


const sideMenu = $('.ui.sidebar').sidebar({
	transition: 'overlay'
})

$('.burger').on('click', function () {
	sideMenu.sidebar('toggle');
});

/*
onVisible($('.ui.sidebar'), () => {
  $('body.pushable>.pusher').css('overflow-y', 'hidden')
})
onHide($('.ui.sidebar'), () => {
  $('body.pushable>.pusher').css('overflow-y', 'auto')
})

I fully give up on trying to stop scroll :/ 
*/
