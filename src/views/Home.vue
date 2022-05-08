<template>
  <div>
    <div>
      <div class="page-title">
        <h3>Добро пожаловать {{ name }} </h3>
        <button class="btn waves-effect waves-light btn-small" @click="refresh">
          <i class="material-icons">refresh</i>
        </button>
      </div>

      <Loader v-if="loading"/>

      <div v-else class="row">
        <MainContent />
      </div>

    </div>
  </div>
</template>

<script>

import Loader from '@/components/app/Loader'
import MainContent from '@/components/Home/MainContent'

export default {
  name: "Home",
  components:  {
    Loader,
    MainContent
  },
  
  data: () => ({
    loading: false,
    currency: null
  }),
  async mounted() {
    this.loading = false
  },
  methods: {
     refresh() {
       this.loading = true 
       setTimeout(() => {
          this.loading = false 
       }, 2000);
    }
  }, 
  computed: {
    name() {
      return this.$store.getters.info.name
    }
  }
};
</script>
