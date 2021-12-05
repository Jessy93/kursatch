<template>
    <div>
        <progress :value="UploadValue" max="100" height="40" id="uploader"></progress><br/>
        <input type="file" @change="onFileSelected" />
        <button @click="onUpload ? onFileSelected(event) : onFileSelected">Upload</button>
        <img width="320" :src="picture" />
        <div v-for="video in videos" :key="video.id" style="display:flex">
            <img :src="video" style="witdh:200px; height: 200px"/>
        </div>
    </div>
</template>

<script>
import firebase from 'firebase'
// import { mapGetters } from "vuex"

export default {
    data: () => ({
        picture: null,
        selectedFile: null,
        UploadValue: 0,
        videos: []
    }),
    // computed: mapGetters(["getVideos"]),
    methods: {
        onFileSelected(event) {
            this.selectedFile = event.target.files[0]
        },
        onUpload() {
            const storageRef = firebase.storage().ref(`/uploads/mediavideo/${this.selectedFile.name}`)
            const task = storageRef.put(this.selectedFile)
            task.on('state_changed', snapshot => {
                let percentage = (snapshot.bytesTransferred / snapshot.totalBytes) * 100;
                this.UploadValue = percentage;
            }, error => { console.log(error.message) },
            () => { this.UploadValue = 100;
                //dowlooadURL
                //task.snapshot.ref.getDownloadURL().then((url) => {
                storageRef.getDownloadURL().then((url) => {
                    this.picture = url;
                    console.log(this.picture)
                });
            });
        },
    },
    mounted() {

        let videosEx = []
        let i = 0
        const storageRef = firebase.storage().ref();
        const listRef =  storageRef.child('uploads/mediavideo');
        listRef.listAll().then((res) => {
            res.items.forEach((itemRef) => {
                i += i
                displayImage(i, itemRef)
          });
        this.videos = videosEx
        console.log(this.videos);
        return this.videos

        }).catch((e) => {
          console.log(e);
        });
        function displayImage(row, images) {
            images.getDownloadURL().then(function (url) {
                videosEx.push(url)
            })
        }
        
    },
}
</script>