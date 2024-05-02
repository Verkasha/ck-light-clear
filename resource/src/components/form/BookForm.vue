<template>
    <v-form @submit.prevent="submit" class="d-flex flex-column ga-4">
        <v-text-field
            label="Название"
            variant="outlined"
            hide-details="auto"
            v-model="form.title"
        />
      <v-text-field
            label="Автор"
            variant="outlined"
            hide-details="auto"
            type="text"
            v-model="form.author"
        />
      <v-text-field
            label="Страна"
            variant="outlined"
            hide-details="auto"
            type="text"
            v-model="form.country"
            />
      <v-text-field
            label="ISBN"
            variant="outlined"
            hide-details="auto"
            type="text"
            v-model="form.isbn"
        />
      <v-text-field
            label="Год"
            variant="outlined"
            hide-details="auto"
            type="number"
            v-model="form.year"
        />


        <v-btn type="submit" hide-details="auto" color="green" variant="outlined">
            {{ btn }}
        </v-btn>
    </v-form>
</template>

<script setup>
defineProps({
    'form': Object,
    'btn': String
})

const emit = defineEmits(['submit'])

const submit = () => {
    emit('submit')
}
</script>
