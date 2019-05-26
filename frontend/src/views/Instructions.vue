<template>
  <view-template class="bg-primary">
    <template #header>
      <b-row align-h="center">
        <b-col tag="figure" cols="6">
          <b-img-lazy
            class="bg-white rounded-circle"
            :src="family"
            fluid
          ></b-img-lazy>
        </b-col>
      </b-row>
    </template>
    <b-row>
      <b-col>
        <ul class="list-unstyled text-white">
          <li v-for="(step, i) in steps" :key="`step-${i}`">
            <h1>
              <em>{{ i + 1 }}.</em>
            </h1>
            <p v-html="step" class="lead"></p>
          </li>
        </ul>
      </b-col>
    </b-row>
    <template #footer>
      <b-row>
        <b-col>
          <b-button variant="outline-light" to="/upload">Got It</b-button>
        </b-col>
      </b-row>
    </template>
  </view-template>
</template>

<script>
  import family from "@/assets/images/svg/family.svg";

  import ViewTemplate from "@/components/ViewTemplate";

  export default {
    components: {
      ViewTemplate
    },

    data: () => ({
      family,
      steps: [
        "Snap a picture or select one from your library.",
        "Select a style.",
        "Share or download your styled image."
      ]
    })
  };
</script>
