<template>
   <div>
        <!--<div>
            <progress :value="UploadValue" max="100" height="40" id="uploader"></progress><br/>
            <input type="file" @change="onFileSelected" />
            <button @click="onUpload">Upload</button>
            <div v-if="picture">
                <img width="320" :src="picture" />
            </div>
        </div>
        <div v-if="getVideos" class="container-videos">
            <div v-for="video in getVideos" :key="video.id" class="video">
                <video controls width="250">
                    <source :src="video" type="video/webm">
                    <source :src="video" type="video/mp4">
                    <!- Sorry, your browser doesn't support embedded videos. ->
                </video>
                <!- <img :src="video"> ->
            </div>
            <div class="video">
                <video id="video" class="video" muted="" poster="https://msk.rtsp.me/v0ePbk4kBL1tZTsehYZopQ/1621841590/poster/KPbwo57M.jpg" src="blob:https://rtsp.me/522d5e7a-bc47-4dc3-ad4a-b8183b44e654" style="opacity: 1;"></video>
            </div>
        </div>-->
        <!-- <div>
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
        </div> -->
        <div>
            <video
                id="my-video"
                class="video-js"
                controls
                preload="auto"
                width="640"
                height="264"
                poster="MY_VIDEO_POSTER.jpg"
                data-setup="{}"
            >
                <source src="http://158.58.130.148/mjpg/video.mjpg" type="video/mp4" />
                <source src="http://158.58.130.148/mjpg/video.mjpg" type="video/webm" />
                <p class="vjs-no-js">
                To view this video please enable JavaScript, and consider upgrading to a
                web browser that
                <a href="https://videojs.com/html5-video-support/" target="_blank"
                    >supports HTML5 video</a
                >
                </p>
            </video>
            <!-- Then, in the player 
            <video class="video-js vjs-theme-city" ...></video>
            <video src="http://158.58.130.148/mjpg/video.mjpg"></video>-->
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


        // playervideo(id) {
        //     var player = this.$video(id, {}, function onPlayerReady() {
        //         this.play();
        //         this.on("ended", function() {
        //         console.log("Awww...over so soon?!");
        //         });
        //     });
        // }


    },
    async mounted() {
        //console.log("c -->", this.getVideos);
        // this.fetchVideos()
        // console.log("a -->", this.fetchVideos());

        // this.playervideo("example_video_1");
        
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