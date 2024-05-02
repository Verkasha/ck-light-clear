<template>
 <v-list-item>
   <v-list-item-title>
        ID {{ book.id }} | {{ book.title }} {{ book.year }}г.
   </v-list-item-title>
   <v-list-item-subtitle>
      Автор: {{ book.author }} Страна: {{ book.country }} ISBN: {{ book.isbn }}
   </v-list-item-subtitle>
   <template v-slot:append>
        <v-list-item-action>
           <v-btn variant="outlined" density="compact" @click="updatePopup = true" class="mr-3"><v-icon size="14">mdi-pencil</v-icon> редактировать</v-btn>
           <v-btn variant="outlined" density="compact" @click="deleteBook"><v-icon size="14">mdi-trash-can</v-icon> удалить</v-btn>
       </v-list-item-action>
   </template>
   <Load v-model="loading"/>
   <BookUpdatePopup v-model="updatePopup" :book="book"/>
 </v-list-item>
</template>

<script setup>
import {useBooksStore} from "@/store/books";
import {ref} from "vue";
import axios from "@/axiosConfig";
import BookUpdatePopup from "@/components/popup/BookUpdatePopup.vue";

const props = defineProps({
  'book': Object
})

const booksStore = useBooksStore()


const updatePopup = ref(false)
const loading = ref(false)

const deleteBook = () => {
  loading.value = true
  axios.delete(`/book/${props.book.id}`)
    .finally(() => {
      booksStore.update()
      loading.value = false
  })
}
</script>
