<template>
  <view-template>
    <template #header>
      <b-row>
        <b-col>
          <h1>
            <strong><em>Share</em></strong>
          </h1>
          <p class="lead">Share or download your styled image.</p>
        </b-col>
      </b-row>
    </template>

    <b-row>
      <b-col>
        <b-card
          v-if="!result"
          border-variant="secondary"
          class="border-dashed vh-50"
        >
          <b-row class="h-100" align-h="center" align-v="center">
            <b-col class="text-center">
              <fa-icon class="text-secondary" size="2x" icon="spinner" spin />
            </b-col>
          </b-row>
        </b-card>
        <b-img v-else :src="result" fluid thumbnail> </b-img>
      </b-col>
    </b-row>

    <template #footer>
      <b-row>
        <b-col>
          <b-button to="/style" variant="outline-dark" class="mr-3"
            >Choose another style</b-button
          >
          <b-button to="/upload" variant="primary">Start Over</b-button>
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
      result() {
        try {
          const { styledImage } = this.$store.state;
          const url = URL.createObjectURL(styledImage);
          return url;
        } catch (error) {
          // console.error(error);
          return null;
        }
      }
    }
  };
</script>
