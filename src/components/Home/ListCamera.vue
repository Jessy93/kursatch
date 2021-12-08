<template>
    <div class="row">
      <video v-for="i in 6" :key="i"
      id="example_video_1"
      class="col video-js vjs-default-skin"
      controls
      preload="auto"
      poster="http://vjs.zencdn.net/v/oceans.png"
      data-setup="{}"
      >
        <!-- <source :src="http://158.58.130.148/mjpg/video.mjpg"> -->
      </video>
    </div>
</template>

<script>


export default {
  name: 'ListCamera',
  data: () => ({

  })
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