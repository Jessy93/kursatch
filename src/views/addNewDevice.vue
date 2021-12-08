<template>
   <div>
        <div>
            <video
            id="example_video_1"
            class="video-js vjs-default-skin"
            controls
            preload="auto"
            width="1280"
            height="720"
            poster="http://vjs.zencdn.net/v/oceans.png"
            data-setup="{}"
            >
            <source src="http://158.58.130.148/mjpg/video.mjpg">
            </video>
        </div>
   </div>
</template>

<script>
import { mapActions, mapGetters, mapMutations } from "vuex";
import firebase from 'firebase'


export default {
    data: () => ({
        picture: null,
        selectedFile: null,
        UploadValue: 0,
    }),
    computed: {
        ...mapGetters(["getVideos"]),
        // getVideos() {
        //     return this.$store.getters.getVideos
        // }
    },
    methods: {

        ...mapActions(["fetchVideos"]),
         ...mapMutations(["updateVideoList"]),
        onFileSelected(event) {
            this.selectedFile = event.target.files[0]
        },
        onUpload() {
            if(this.selectedFile === null) {
                console.log('vide -->', this.selectedFile)
                return
            } else {
                const storageRef = firebase.storage().ref(`/uploads/mediavideo/${this.selectedFile.name}`)
                const task = storageRef.put(this.selectedFile)
                task.on('state_changed', snapshot => {
                    let percentage = (snapshot.bytesTransferred/snapshot.totalBytes) * 100;
                    this.UploadValue = percentage;
                }, error => { console.log(error.message) },
                () => { this.UploadValue = 100;
                    //dowlooadURL
                    //console.log(snapshot)
                    task.snapshot.ref.getDownLoadURL().then((url) => {
                        this.picture = url;
                        console.log(this.picture)
                    });
                });
            }
            
        },
    },
    async mounted() {}
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