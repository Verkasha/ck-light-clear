<template>
    <v-overlay class="d-flex align-center justify-center" width="400" @click:outside="close">
        <v-sheet class="pa-8 d-flex flex-column ga-4" rounded>
            <Error :error="error"/>
            <div class="d-flex justify-between align-top mb-5">
                <div class="text-left">
                    <div class="text-lg font-bold">Изменение книги</div>
                </div>
            </div>
            <BookForm :form="form" @submit="submit" btn="Изменить книги"/>
        </v-sheet>
    </v-overlay>
</template>


<script setup>
import BookForm from "@/components/form/BookForm.vue";
import {reactive, ref} from "vue";
import axios from "@/axiosConfig";
import {useBooksStore} from "@/store/books";

const emit = defineEmits(["update:modelValue"]);

const props = defineProps({
  'book': Object
})

const booksStore = useBooksStore()

const error = ref('')



const form = reactive({
    'title': props.book?.title ?? '',
    'year': props.book?.year ?? '',
    'author' : props.book?.author ?? '',
    'country' : props.book?.country ?? '',
    'isbn' : props.book?.isbn ?? ''
  })
function submit(){
  error.value = ''
  axios.put(`/book/${props.book.id}`,form).then((reason) => {
    booksStore.update()
    close()
    console.log(reason.data)
  }).catch((reason) => {
    if (reason.response){
          error.value = reason.response.data
    }
    console.log(reason)
  })
}

function close(){
    emit("update:modelValue", false);
}


</script>

<style lang="scss">

</style>
