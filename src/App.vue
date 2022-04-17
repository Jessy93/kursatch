<template>
  <div id="app">
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>
import hls from "./utils/hls"
import EmptyLayout from "@/layouts/EmptyLayout";
import MainLayout from "@/layouts/MainLayout";


export default {
  // rtsp://91.222.130.82:8554/ch1
  computed: {
    layout() {
      return (this.$route.meta.layout || "empty") + "-layout";
    },
  },
  components: {
    EmptyLayout,
    MainLayout,
  },
  // mounted() {
  //   // HLS First  option Doesnt work-->
  //   if (document.getElementById('hls-coding')) {
  //     return;} else {
  //     var scriptTag = document.createElement("script");
  //     scriptTag.src = hls;
  //     scriptTag.id = "hls-coding";
  //     document.getElementsByTagName('head')[0].appendChild(scriptTag);
  //   }
  // }
}

</script>


<style lang="scss">
@import "~materialize-css/dist/css/materialize.min.css";
@import "assets/index.css";
.btn {
  text-transform: capitalize !important;
  box-shadow: none !important;
}
</style>
