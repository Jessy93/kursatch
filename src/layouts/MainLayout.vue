<template>
  <div>
    <Loader v-if="loading"/>

    <div class="app-main-layout" v-else>
      <Navbar @click="isOpen = !isOpen"/>
      <Sidebar v-model="isOpen"/>

      <main class="app-content" :class="{full: !isOpen}">
        <div class="app-page">
          <router-view />
        </div>
      </main>

      <div class="fixed-action-btn">
        <a class="waves-effect waves-circle btn modal-trigger btn-floating btn-large blue" href="#modal1">
          <i class="large material-icons">add</i>
        </a>
      </div>

      <!-- Modal Structure -->
      <div id="modal1" class="modal" ref="modal">
        <div class="modal-content">
          <h4 class="orange-text">Выберите файл для архивации</h4>
          <p>После загрузки файла на сервер, вы сможете зашифровать или расшифровать его по желанию</p>

          <form action="#">
            <div class="file-field input-field">
              <div class="orange btn">
                <i class="material-icons">attach_file</i>
                <span>файл</span>
                <input type="file" id="file" @change="handleFileUpload($event)">
              </div>
              <div class="file-path-wrapper">
                <input class="file-path validate">
              </div>
            </div>
          </form>
        </div>
        <div class="modal-footer">
          <div class="waves-effect green darken-1 btn" :disabled="!this.file" @click="submitFile()">
            <i class="material-icons left">file_upload</i>
            загрузить
          </div>
          <div class="modal-close btn red lighten-1">
            <i class="material-icons left">cancel</i>
            Отменить
          </div>
        </div>
      </div>

    </div>
  </div>
</template>

<script>

import axios from 'axios';

import Navbar from '@/components/app/Navbar'
import Sidebar from '@/components/app/Sidebar'
import Loader from '@/components/app/Loader'

export default {
  name: 'main-layout',
  components: {Navbar, Sidebar, Loader},
  data: () => ({
    isOpen: true,
    loading: false,
    isOpenModal: false,
    instance: null,
    file: '',
    url: 'http://localhost:5000/models/upload',
  }),
  methods: {
    handleFileUpload (event) {
      this.file = event.target.files[0];
    },
    submitFile () {
      let formData = new FormData();
      formData.append('file', document.querySelector('#file').files[0]);
      
      for (var value of formData.values()) {
        console.log(1, value);
      }
      
      axios.post(this.url, formData, {headers:{'Content-Type': 'multipart/form-data'}})
        .then(res => {
          console.log(100, res)
        })
        .catch (err => {
          console.log(101, err);
        })
    },
  },
  async mounted() {
    if (!Object.keys(this.$store.getters.info).length) {
     await this.$store.dispatch('fetchInfo');
     this.loading = false;
    };
    // initialisation de la boite modale
    this.instance = M.Modal.init(this.$refs.modal);


    // document.addEventListener('DOMContentLoaded', function() {
    //   var elems = document.querySelectorAll('.modal');
    //   var instances = M.Modal.init(elems, options);
    // });


  },
}
</script>

<style lang="scss">


.modal {
  max-height: 77% !important;
  &-content {
    padding: 24px 24px 0px 24px !important;
  }
  &-footer, .btn {
    display: flex;
    justify-content: space-evenly;
    align-items: center;
  }
}
</style>
