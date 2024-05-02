<script setup>
defineProps({
    'error': String
})
</script>

<template>
            <v-alert v-if="error" color="red" variant="flat" class="overflow-auto" style="max-height: 150px">
              <h4>Ошибка</h4>
              <pre class="overflow-auto">{{ error }}</pre>
            </v-alert>
</template>

<style scoped>

</style>
