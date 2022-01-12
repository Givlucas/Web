$(document).ready(function(){

    var audioEle = document.createElement('audio');
    audioEle.setAttribute('src', 'http://home.otmlabs.xyz:60000/audio.ogg')
    var currentStation = ""

    $('#play').on('click', function(e) {
      audioEle.play()
      });

      $('#pause').on('click', function(e) {
        audioEle.pause()
        });

    $('#1027').on('click', function(e) {
      audioEle.setAttribute('src', 'http://home.otmlabs.xyz:60000/audio.ogg')
      audioEle.play()
      currentStation = "1027"
      e.preventDefault()
      $.getJSON('/1027',
          function(data){
            // do nothing
          });
          return false;
      });

    $('#999').on('click', function(e) {
      audioEle.setAttribute('src', 'http://home.otmlabs.xyz:60000/audio.ogg')
      audioEle.play()
      currentStation = "999"
      e.preventDefault()
      $.getJSON('/999',
          function(data){
            // do nothing
          });
          return false;
      });

        $('#961').on('click', function(e) {
          audioEle.setAttribute('src', 'http://home.otmlabs.xyz:60000/audio.ogg')
          audioEle.play()
          e.preventDefault()
          $.getJSON('/961',
              function(data){
                // do nothing
              });
              return false;
          });

          $('#1073').on('click', function(e) {
            audioEle.setAttribute('src', 'http://home.otmlabs.xyz:60000/audio.ogg')
            audioEle.play()
            e.preventDefault()
            $.getJSON('/1073',
                function(data){
                  // do nothing
                });
                return false;
            });

});
