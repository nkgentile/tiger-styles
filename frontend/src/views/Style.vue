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
        <b-radio-group
          label="Styles"
          v-model="selectedStyle"
          :options="styles"
          value-field="id"
          text-field="label"
        >
        </b-radio-group>
        <p>{{ selectedStyle }}</p>
      </b-col>
    </b-row>

    <template #footer>
      <b-row>
        <b-col>
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
        { id: "tony", label: "Tony", image: "" },
        { id: "tigris", label: "Tigris", image: "" },
        { id: "stripes", label: "Stripes", image: "" }
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
