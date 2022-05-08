import Vue from 'vue'
import Vuelidate from 'vuelidate'
import App from './App.vue'
import router from './router'
import store from './store'
import dateFilter from '@/filters/date.filter'
import currencyFilter from '@/filters/currency.filter'
import messagePlugin from '@/utils/message.plugin'
import Loader from '@/components/app/Loader'


import './registerServiceWorker'
import 'materialize-css/dist/js/materialize.min'


import firebase from 'firebase/app'
import 'firebase/auth'
import 'firebase/database'
import 'firebase/firestore'

// import axios from 'axios';
// axios.defaults.headers.common['Access-Control-Allow-Origin'] = '*';

Vue.config.productionTip = false

Vue.use(messagePlugin)
Vue.use(Vuelidate)
Vue.filter('date', dateFilter)
Vue.filter('currency', currencyFilter)
Vue.component('Loader', Loader)

firebase.initializeApp({
  apiKey: "AIzaSyB-cv-k2t7XhNCmfINwCSrVCOVYS0d68lk",
  authDomain: "kursatch-1.firebaseapp.com",
  databaseURL: "https://kursatch-1-default-rtdb.firebaseio.com",
  projectId: "kursatch-1",
  storageBucket: "kursatch-1.appspot.com",
  messagingSenderId: "877735595729",
  appId: "1:877735595729:web:05b89bdb1ddcaa0e5bfff0",
  measurementId: "G-82040QBJ03"
})

let app 

firebase.auth().onAuthStateChanged(() => {
  if (!app) {
    app = new Vue({
      router,
      store,
      render: h => h(App)
    }).$mount('#app')
  }
})