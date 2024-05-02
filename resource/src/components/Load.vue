<template>
  <v-overlay
      class="align-center justify-center"
      closeDelay="1"
      :persistent="true"
  >
    <v-progress-circular
        color="blue"
        indeterminate
        size="64"
    ></v-progress-circular>
  </v-overlay>
</template>
