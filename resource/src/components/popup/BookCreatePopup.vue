<template>

    <v-overlay class="d-flex align-center justify-center overflow-auto" width="400" @click:outside="close">
        <v-sheet class="pa-8 d-flex flex-column ga-4" rounded>
            <Error :error="error"/>
            <div class="d-flex justify-between align-top mb-5">
                <div class="text-left">
                    <div class="text-lg font-bold">Форма добавление книги</div>
                </div>
            </div>
            <BookForm :form="form" @submit="submit" btn="Добавить книги"/>
        </v-sheet>
    </v-overlay>
</template>


<script setup>
import BookForm from "@/components/form/BookForm.vue";
import {reactive, ref} from "vue";
import axios from "@/axiosConfig";
import {useBooksStore} from "@/store/books";

const emit = defineEmits(["update:modelValue"]);

const booksStore = useBooksStore()

const error = ref('')

const init = {
    'title': '',
    'year': '',
    'isbn': '',
    'country': '',
    'author': '',
}

const form = reactive({...init})
function submit(){
  error.value = ''
  axios.post('/book/',form).then(() => {
    booksStore.update()
    Object.assign(form, init);
    close()
  }).catch((reason) => {
    if (reason.response){
          error.value = reason.response.data
    }

  })
}

function close(){
    emit("update:modelValue", false);
}


</script>

<style lang="scss">

</style>
