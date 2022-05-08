<template>
    <div class="row">
        <VideoPlayer :videoURL="videoURL"></VideoPlayer>

        <!-- <video-embed :params="{autoplay: 1}" src="http://honjin1.miemasu.net/nphMotionJpeg?Resolution=640x480&Quality=Standard"></video-embed> -->
        <!-- <video src="http://honjin1.miemasu.net/nphMotionJpeg?Resolution=640x480&Quality=Standard"></video> -->
    </div>
</template>

<script>
import VideoPlayer from '@/components/VideoPlayer.vue';

export default {
  name: 'ListCamera',
   components:  {VideoPlayer},
  data: () => ({
      videoURL: 'rtsp://root:admin@91.222.130.82:3554/axis-media/media.amp'
  }),
  methods: {

  },
  mounted () {

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