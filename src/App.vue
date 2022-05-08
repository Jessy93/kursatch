<template>
  <div id="app">
    <component :is="layout">
      <router-view />
    </component>
  </div>
</template>

<script>

import EmptyLayout from '../src/layouts/EmptyLayout.vue'
import MainLayout from '../src/layouts/MainLayout.vue'
export default {
  computed: {
    layout() {
      return (this.$route.meta.layout || "empty") + "-layout";
    },
  },
  components: {
    EmptyLayout,
    MainLayout,
  },
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
