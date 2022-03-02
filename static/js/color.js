const bt = document.querySelector('.color-shifter');

let state = 0;

bt.addEventListener('click', () => {
  if(state % 3 == 0){
    $(".asset").addClass('d-asset');
    $(".asset-ele").addClass('d-asset-ele-b');
    $(".b").removeClass('rainbow-body');
    $(".b").addClass('d-body');
    state += 1;
  }
  else if(state % 3 == 1){
    $(".asset").removeClass('d-asset');
    $(".b").removeClass('d-body');

    $(".asset").addClass('wb-asset');
    $(".asset-nb").addClass('wb-asset-nb');

    $(".b").removeClass('rainbow-body');
    $(".b").addClass('wb-body');


    state += 1;
  }
  else if(state % 3 == 2){
    $(".asset").removeClass('wb-asset');
    $(".asset-nb").removeClass('wb-asset-nb');
    $(".b").addClass('rainbow-body');
    $(".b").removeClass('wb-body');
    state += 1;
  }

});
