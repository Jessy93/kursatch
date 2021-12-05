<template>
  <div>
    <div>
      <div class="page-title">
        <h3>Hi {{ name }} </h3>

        <button class="btn waves-effect waves-light btn-small" @click="refresh">
          <i class="material-icons">refresh</i>
        </button>
      </div>

      <Loader v-if="loading"/>

      <div v-else class="row">
        <!-- <HomeBill :rates="currency.rates"/>
        <HomeCurrency :rates="currency.rates" :date="currency.date"/> -->
        <OngletPrincipal />
        <MainContent />
        <DeviceSidebar />
      </div>
    </div>
  </div>
</template>

<script>
// import HomeBill from '@/components/HomeBill'
// import HomeCurrency from '@/components/HomeCurrency'

import OngletPrincipal from '@/components/Home/OngletPrincipal'
import MainContent from '@/components/Home/MainContent'
import DeviceSidebar from '@/components/Home/DeviceSidebar'

import Loader from '@/components/app/Loader'
export default {
  name: "Home",
  components:  {
    OngletPrincipal, MainContent, DeviceSidebar, Loader
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
