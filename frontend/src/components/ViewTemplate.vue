<template>
  <article class="view-template vh-100 p-3">
    <b-container tag="header" class="view-template-header" fluid>
      <b-row align-h="center">
        <b-col sm="12" md="4">
          <slot name="header" />
        </b-col>
      </b-row>
    </b-container>
    <b-container
      tag="main"
      class="view-template-content"
      :class="$style[align]"
      fluid
    >
      <b-row align-h="center">
        <b-col sm="12" md="4">
          <slot />
        </b-col>
      </b-row>
    </b-container>
    <b-container tag="footer" class="view-template-footer" fluid>
      <b-row align-h="center">
        <b-col sm="12" md="4">
          <slot name="footer" />
        </b-col>
      </b-row>
    </b-container>
  </article>
</template>

<script>
  export default {
    props: {
      align: {
        type: String,
        default: "start",
        validator(value) {
          return ["start", "center", "end"].includes(value);
        }
      }
    }
  };
</script>

<style lang="scss" module>
  $alignments: "start", "center", "end";

  @each $alignment in $alignments {
    .#{$alignment} {
      align-self: #{$alignment};
    }
  }
</style>

<style lang="scss" scoped>
  .view-template {
    display: grid;
    grid-template-rows: auto 1fr auto;
    grid-gap: 1rem;
  }
</style>