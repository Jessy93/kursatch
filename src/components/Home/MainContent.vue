<template>
  <div class="card">
    <span class="card-title orange-text">Управление устройства (Камера)</span>
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
  .bill-card {
    height: 555px;
  }
</style>