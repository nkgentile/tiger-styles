<template>
  <view-template>
    <template #header>
      <b-row>
        <b-col>
          <h1>
            <strong><em>Style</em></strong>
          </h1>
          <p class="lead">Select a style.</p>
        </b-col>
      </b-row>
    </template>

    <b-row>
      <b-col>
        <template v-for="{ id, label, image } in styles">
          <b-card
            v-if="selectedStyle === id"
            :key="id"
            class="my-1"
            :img-src="image"
            border-variant="primary"
            :header="label"
            header-bg-variant="primary"
            header-text-variant="white"
            no-body
          >
          </b-card>
          <b-card
            v-else
            :key="id"
            :img-src="image"
            class="my-1"
            :header="label"
            no-body
            @click="selectedStyle = id"
          >
          </b-card>
        </template>
      </b-col>
    </b-row>

    <template #footer>
      <b-row>
        <b-col col>
          <b-button to="/upload" variant="outline-secondary">Back</b-button>
        </b-col>
        <b-col class="text-right" cols="6">
          <b-button to="/share" variant="primary">Submit</b-button>
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
    data: () => ({
      styles: [
        {
          id: "tony",
          label: "Tony",
          image: require("@/assets/images/jpg/tony.jpg")
        },
        {
          id: "tigris",
          label: "Tigris",
          image: require("@/assets/images/jpg/tigris.jpg")
        },
        {
          id: "stripes",
          label: "Stripes",
          image: require("@/assets/images/jpg/stripes.jpg")
        }
      ]
    }),
    computed: {
      selectedStyle: {
        get() {
          return this.$store.state.style;
        },
        set(id) {
          this.$store.commit("setStyle", {
            id
          });
        }
      }
    }
  };
</script>
