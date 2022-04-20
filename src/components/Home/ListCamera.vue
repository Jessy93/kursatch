<template>
    <div class="row">
        
    </div>
</template>

<script>

export default {
  name: 'ListCamera',
  data: () => ({
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