<template>
  <div>
    <h5 class="card-title orange-text">Управление устройства (Камера)</h5>
    <Devices />
  </div>
</template>

<script>
import Devices from '@/components/Home/Devices'

export default {
  name: 'MainContent',
  components:  {Devices},
}
</script>

<style scoped>
  .card-title.orange-text {
    font-size: 24px;
    font-weight: 300;
  }
</style>