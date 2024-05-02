<template>
  <div class="ma-5">
    <v-card>
      <div class="d-flex justify-space-between align-center mr-5 py-3">
        <v-card-title>Книги</v-card-title>
        <div class="d-flex align-center justify-space-between">
          <v-btn variant="flat" class="mr-4" @click="update">Обновить список</v-btn>
          <v-btn color="primary" @click="createPopup = true">Добавить книгу</v-btn>
        </div>
      </div>
    <v-list v-if="!loading">
      <BookItem v-for="book in books" :book=book :key="book.id"/>
      <div class="text-center mb-4" v-if="books.length === 0">В базе данных нет книг.</div>
    </v-list>
      <v-card-text v-else class="d-flex justify-center my-10">
        <v-progress-circular color="primary" indeterminate :size="60"></v-progress-circular>
      </v-card-text>
    </v-card>
  </div>
  <BookCreatePopup v-model="createPopup"/>
</template>

<style scoped>

</style>

<script setup>
import {computed, onMounted, ref} from "vue";
import {useBooksStore} from "@/store/books";
import BookCreatePopup from "@/components/popup/BookCreatePopup.vue";

const createPopup = ref(false)

const booksStore = useBooksStore()

const loading =  computed(() => {
  return booksStore.loading
});
const books = computed(() => {
  return booksStore.books
});

const update = () => {
    if(!loading.value){
          booksStore.update()
    }
}

onMounted(() => {
  update()
})
</script>

