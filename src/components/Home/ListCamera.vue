<template>
    <div class="row">
      <!-- Scd option does not work -->
      <!-- <div class="fp-Video">
        <div id="myVideo" class="display"></div>
      </div>
      <br />
      <button id="playBtn" @click="alloh()">PLAY</button> -->


      <div class="jsmpeg" data-url="rtsp://91.222.130.82:8554/ch1"></div>


    </div>
</template>

<script>
// import hls from "@/utils/hls"
// import Flashphoner from "@/utils/flashphoner"
// import jsmpeg from "@/utils/jsmpeg"

export default {
  name: 'ListCamera',
  data: () => ({
  }),
  methods:  {
    //   alloh () {
    //     init_api()
    //     //Status constants
    //     var SESSION_STATUS = Flashphoner.constants.SESSION_STATUS;
    //     var STREAM_STATUS = Flashphoner.constants.STREAM_STATUS;
    //     var session;
    //     var PRELOADER_URL = "https://github.com/flashphoner/flashphoner_client/raw/wcs_api-2.0/examples/demo/dependencies/media/preloader.mp4";
        
    //     //Init Flashphoner API on page load
    //     function init_api() {
    //         Flashphoner.init({});
    //         //Connect to WCS server over websockets
    //         session = Flashphoner.createSession({
    //             urlServer: "ws://192.168.1.6:8080" //specify the address of your WCS
    //         }).on(SESSION_STATUS.ESTABLISHED, function(session) {
    //             console.log("ESTABLISHED");
    //         });
        
    //         playClick();
    //     }
        
    //     //Detect browser
    //     var Browser = {
    //         isSafari: function() {
    //             return /^((?!chrome|android).)*safari/i.test(navigator.userAgent);
    //         },
    //     }
    //     /**
    //     *
    //     If browser is Safari, we launch the preloader before playing the stream.
    //     Playback should start strictly upon a user's gesture (i.e. button click). This is limitation of mobile Safari browsers.
    //     https://docs.flashphoner.com/display/WEBSDK2EN/Video+playback+on+mobile+devices
    //     *
    //     **/
    //     function playClick() {
    //         if (Browser.isSafari()) {
    //             Flashphoner.playFirstVideo(document.getElementById("play"), true, PRELOADER_URL).then(function() {
    //                 playStream();
    //             });
    //         } else {
    //             playStream();
    //         }
    //     }
        
    //     //Playing stream
    //     function playStream() {
    //         session.createStream({
    //             name: "rtsp://91.222.130.82:8554/ch1", //specify the RTSP stream address
    //             display: document.getElementById("myVideo"),
    //         }).play();
    //     }

    // },
    benson () {
        var video = document.getElementById('video');
        var videoSrc = 'rtsp://91.222.130.82:8554/ch1';
        if (Hls.isSupported()) {
            var hls = new Hls();
            hls.loadSource(videoSrc);
            hls.attachMedia(video);
        }
        
        else if (video.canPlayType('application/vnd.apple.mpegurl')) {
            video.src = videoSrc;
        }
    }
  },
  mounted () {
      // hls first option
    if (document.getElementById('hls-coding')) {
        console.log(1);
        this.benson();
    } else {
        console.log(2);
        var scriptTag = document.createElement("script");
        scriptTag.src = hls;
        scriptTag.id = "hls-coding";
        document.getElementsByTagName('head')[0].appendChild(scriptTag);
        
    }


    // flashphoner // Scd option does not work
    //   if (document.getElementById('flashphoner-coding')) {
    //     console.log(1);
    //     // this.alloh();
    //   } else {
    //     console.log(2);
    //     var scriptTag = document.createElement("script");
    //     scriptTag.src = Flashphoner;
    //     scriptTag.id = "flashphoner-coding";
    //     document.getElementsByTagName('head')[0].appendChild(scriptTag);
        
    //   }

    // jsmpeg
    // if (document.getElementById('jsmpeg-coding')) {
    //     console.log(1);
    //     // this.alloh();
    // } else {
    //     console.log(2);
    //     var scriptTag = document.createElement("script");
    //     scriptTag.src = jsmpeg;
    //     scriptTag.id = "jsmpeg-coding";
    //     document.getElementsByTagName('head')[0].appendChild(scriptTag);
        
    // }
  }
}
</script>

<style scoped>

.container-videos {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
}
.video {
    width: 200px;
    height: 200px;
    margin: 20px;
}
.video video {
    width: 200px;
    height: 200px;
    object-fit: revert;
    object-position: center;
}
</style>