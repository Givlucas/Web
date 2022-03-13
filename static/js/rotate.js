let c = 45;

function draw(){
  document.documentElement.style.setProperty('--direction', (c+=0.25) + 'deg');
  requestAnimationFrame(draw);
}

requestAnimationFrame(draw);
