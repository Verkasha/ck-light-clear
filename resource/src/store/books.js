import { defineStore } from 'pinia'
import axios from "@/axiosConfig";

export const useBooksStore = defineStore('books', {
  state: () => ({
      loading: false,
      books: []
    }),
  actions: {
    update() {
      this.loading = true
      axios.get('/book/').then( (response) => {
        this.books = response.data
      })
      console.log(this.books)
      this.loading = false
    }
  }
})
