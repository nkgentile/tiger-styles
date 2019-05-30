<template>
  <view-template class="bg-dark">
    <template #header>
      <b-row>
        <b-col class="text-white">
          <h1>
            <strong><em>Upload</em></strong>
          </h1>
          <p class="lead">Snap a picture or select one from your library.</p>
        </b-col>
      </b-row>
    </template>

    <b-row>
      <b-col>
        <b-card
          v-if="!image"
          bg-variant="dark"
          border-variant="secondary"
          class="border-dashed vh-50"
        >
          <b-row class="h-100" align-h="center" align-v="center">
            <b-col class="text-center">
              <fa-icon class="text-secondary" size="3x" icon="portrait" />
            </b-col>
          </b-row>
        </b-card>
        <b-img v-else :src="image" fluid thumbnail> </b-img>
        <b-file v-model="file"></b-file>
      </b-col>
    </b-row>

    <template #footer>
      <b-row>
        <b-col class="text-right">
          <b-button to="/style" variant="outline-light">Next</b-button>
        </b-col>
      </b-row>
    </template>
  </view-template>
</template>

<script>
  import ViewTemplate from "@/components/ViewTemplate";

  export default {
    components: {
      ViewTemplate
    },

    computed: {
      file: {
        get() {
          return this.$store.state.originalImage;
        },
        set(file) {
          this.$store.commit("setOriginalImage", {
            file
          });
        }
      },

      image() {
        try {
          const url = URL.createObjectURL(this.file);
          return url;
        } catch (error) {
          // console.error(error);
          return null;
        }
      }
    }
  };
</script>
