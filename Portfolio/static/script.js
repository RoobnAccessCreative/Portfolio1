function check(v="You're code is bootiful") {
  // A general check that can be inserted anywhere
  console.log(v)
}


const item = $('a.item');

const sideMenu = $('.ui.sidebar').sidebar({
	transition: 'overlay',
  scrollLock: true // supposed to disable page scroll, probably does nothing lol
});

$('.burger').on('click', function () {
	sideMenu.sidebar('toggle');
});


