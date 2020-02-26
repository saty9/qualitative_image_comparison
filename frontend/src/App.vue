<template>
    <div id="app">
        <div v-if="just_started">
            Tap the image you think looks most likely to be an antique map of the source area shown
            <button @click="just_started = false">Get Started</button>
        </div>
        <div v-else-if="index<image_list.length">
            src:<img v-bind:src="'/back/static/data/' + image_list[index] + '/src.png'"><br>
            A:<img v-bind:src="'/back/static/data/' + image_list[index] + '/'+ (flipped ? 'A': 'B') + '.png'"
                   @click="img_clicked('A')"><br>
            B:<img v-bind:src="'/back/static/data/' + image_list[index] + '/'+ (flipped ? 'B': 'A') + '.png'"
                   @click="img_clicked('B')"><br>
        </div>
        <div v-else>
            Thanks!
        </div>
        <div style="visibility: hidden">
            <img v-bind:src="i.src" v-for="i in prefetched" v-bind:key="i.src">
        </div>
    </div>
</template>

<script>

  export default {
    name: 'App',
    components: {},
    data: function () {
      return {
        image_list: [],
        index: 0,
        just_started: true,
        flipped: false,
        prefetched: []
      };
    },
    mounted: function () {
      let self = this;
      this.axios.get("/back/list").then(function (response) {
        if (response.status == 200) {
          self.$data.image_list = response.data.files;
          self.preload(self.image_list);
        }
      })
    },
    methods: {
      img_clicked: function (letter) {
        if (letter == 'A' && this.flipped) {
          letter = 'B'
        } else if (letter == 'B' && this.flipped) {
          letter = 'A'
        }
        this.axios.post('/back/result/' + this.image_list[this.index], {result: letter});
        this.flipped = Math.random() >= 0.5;
        this.index++;
      },
      preload: function () {
        let self = this;
        for (var i = 0; i < arguments[0].length; i++) {
          // eslint-disable-next-line no-unused-vars
          let images = new Image();
          images.src = '/back/static/data/' + arguments[0][i]  + '/src.png';
          // eslint-disable-next-line no-unused-vars
          let imagea = new Image();
          imagea.src = '/back/static/data/' + arguments[0][i] + '/A.png';
          // eslint-disable-next-line no-unused-vars
          let imageb = new Image();
          imageb.src = '/back/static/data/' + arguments[0][i] + '/B.png';
          self.prefetched.push(images);
          self.prefetched.push(imagea);
          self.prefetched.push(imageb);
        }
      }
    }
  }
</script>

<style>
    #app {
        font-family: Avenir, Helvetica, Arial, sans-serif;
        -webkit-font-smoothing: antialiased;
        -moz-osx-font-smoothing: grayscale;
        text-align: center;
        color: #2c3e50;
    }

    img {
        max-height: 29vh;
        width: auto;
    }
</style>
