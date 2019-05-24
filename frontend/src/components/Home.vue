
<template>
  <div>
    <div>
      </br>
      <p>Home page</p>
      <p>Random number from backend: {{ randomNumber }}</p>
      <button @click="getRandom">New random number</button>
    </div>
    </br>
    <div class="container">
      <div class="large-12 medium-12 small-12 cell">
        <label>File Preview
          <input type="file" id="file" ref="file" accept="image/*" v-on:change="handleFileUpload()" />
        </label>
        <img v-bind:src="imagePreview" v-show="showPreview" />
        <label>StyleID
          <input type="text" v-model="styleType" placeholder="style type" />
        </label>
        <button v-on:click="submitFile()">Submit</button>
        <p>STYLEID from backend: {{styleID}}</p>
      </div>

    </div>

  </div>
</template>

<script>
import axios from 'axios'
export default {
  data() {
    return {
      randomNumber: 0,
      file: '',
      showPreview: false,
      imagePreview: '',
      styleType: 'tigris',
      message: '',
      styleID: ''
    }
  },
  methods: {
    getRandomInt(min, max) {
      min = Math.ceil(min)
      max = Math.floor(max)
      return Math.floor(Math.random() * (max - min + 1)) + min
    },
    getRandom() {
      // this.randomNumber = this.getRandomInt(1, 100)
      this.randomNumber = this.getRandomFromBackend()
    },
    getRandomFromBackend() {
      const path = `http://localhost:5000/api/random`
      axios.get(path)
        .then(response => {
          this.randomNumber = response.data.randomNumber
        })
        .catch(error => {
          console.log(error)
        })
    },

    submitFile() {
      /*
              Initialize the form data
          */
      let formData = new FormData();

      /*
          Add the form data we need to submit
      */
      formData.append('photoFile', this.file);
      formData.append('style', this.styleType);

      /*
        Make the request to the POST /single-file URL
      */
      axios.post('http://localhost:5000/api/dwim',
        formData,
        {
          headers: {
            'Content-Type': 'multipart/form-data'
          }
        }
      ).then(response => {
        this.styleID = response.data.styleID
        console.log('SUCCESS!!');
        this.file = '';
      })
        .catch(function() {
          console.log('FAILURE!!');
          // this.file = '';
        });
    },

    handleFileUpload() {
      /*
        Set the local file variable to what the user has selected.
      */
      this.file = this.$refs.file.files[0];

      /*
        Initialize a File Reader object
      */
      let reader = new FileReader();

      /*
        Add an event listener to the reader that when the file
        has been loaded, we flag the show preview as true and set the
        image to be what was read from the reader.
      */
      reader.addEventListener("load", function() {
        this.showPreview = true;
        this.imagePreview = reader.result;
      }.bind(this), false);

      /*
        Check to see if the file is not empty.
      */
      if (this.file) {
        /*
          Ensure the file is an image file.
        */
        if (/\.(jpe?g|png|gif)$/i.test(this.file.name)) {
          /*
            Fire the readAsDataURL method which will read the file in and
            upon completion fire a 'load' event which we will listen to and
            display the image in the preview.
          */
          reader.readAsDataURL(this.file);

        }
      }
    }

  },
  created() {
    this.getRandom()
  }
}
</script>

<style>
div.container img {
  max-width: 200px;
  max-height: 200px;
}
</style>

