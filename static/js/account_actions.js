const da = document.querySelector('.activate');
const popup = document.querySelector('.pop-up-bg')
const no = document.querySelector('.no')
let open = false;

da.addEventListener('click', () => {
    popup.classList.add('display-popup');
    open = true;
});

no.addEventListener('click', () => {
    popup.classList.remove('display-popup');
});
