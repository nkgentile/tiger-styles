<template>
  <view-template id="start" align="end">
    <b-img
      id="background"
      src="@/assets/images/jpg/landing-background.jpg"
    ></b-img>
    <b-row>
      <b-col>
        <b-img-lazy :src="logo" fluid></b-img-lazy>
        <h1>Tiger Styles</h1>
        <p class="lead">
          Magically personalize your photos, using AI, with styles celebrating
          Princeton Reunion 2019. Have fun with it!
        </p>
      </b-col>
    </b-row>
    <template #footer>
      <b-row>
        <b-col>
          <b-button to="/instructions" variant="primary">Get Started</b-button>
        </b-col>
      </b-row>
      <b-row>
        <b-col>
          <p class="small text-muted">
            Disclaimer: We do not store any personal information, including your
            photos.
          </p>
        </b-col>
      </b-row>
    </template>
  </view-template>
</template>

<script>
  import logo from "@/assets/images/svg/logo.svg";

  import ViewTemplate from "@/components/ViewTemplate";

  export default {
    components: {
      ViewTemplate
    },

    data: () => ({
      logo
    })
  };
</script>

<style lang="scss" scoped>
  #start {
    #background {
      position: fixed;
      z-index: -1;
      top: 0;
      left: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: center;
    }

    &::before {
      content: "";

      display: block;
      position: fixed;

      top: 0;
      left: 0;

      width: 100vw;
      height: 100vh;

      background: linear-gradient(to top, white 45%, rgba(255, 255, 255, 0) 100%);
    }
  }
</style>
