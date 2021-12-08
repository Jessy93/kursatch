<template>
   <div class="col s12 m6 l9">
      <div class="card white darken-3 bill-card">
        <div class="card-content orange-text">
          <div class="card-header">
            <span class="card-title">Управление устройства (Камера)</span>
            <ListCamera />
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import ListCamera from '@/components/Home/ListCamera'

export default {
  name: 'MainContent',
  components:  {ListCamera},
}
</script>

<style scoped>
  .bill-card {
    height: 555px;
  }
</style>