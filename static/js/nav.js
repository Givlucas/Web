const menubtn = document.querySelector('.hamburger');
const nav = document.querySelector('.nav');

let menuOpen = false;

menubtn.addEventListener('click', () => {
  if(!menuOpen) {
    menubtn.classList.add('open');
    nav.classList.add('grow');
    menuOpen = true;
  } else {
    menubtn.classList.remove('open');
    nav.classList.remove('grow');
    menuOpen = false;
  }
});
