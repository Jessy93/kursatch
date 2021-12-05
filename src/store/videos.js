import firebase from 'firebase/app';

export default {
    state: {
      videos: []
    },
    getters: {
      getVideos(state) {
        return state.videos
        //  videos: s => s.videos
      }
    },
    mutations: {
      updateVideoList(state, videos) {
        state.videos = videos
      }
    },
    actions: {
      async fetchVideos(ctx) {
        const storageRef = await firebase.storage().ref("uploads/mediavideo");
        const videos = [];
         storageRef.listAll().then((res) => {
           console.log(res)
           res.items.forEach((itemRef) => {
            itemRef.getDownloadURL().then(function(url) {
              videos.push(url)
            })
          });
        }).catch((e) => {
          console.log(e);
        });
        ctx.commit('updateVideoList', videos)
        console.log("videos", videos);
        // return videos
      }
    },
}