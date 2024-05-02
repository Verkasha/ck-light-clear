import axios from 'axios';

// Настройка базового URL для всех запросов
axios.defaults.baseURL = 'http://127.0.0.1:7500/api/v1/';

// Добавление перехватчика ответов
axios.interceptors.response.use(response => {
  // Ваш код для обработки успешных ответов
  return response;
}, error => {
  // Обработка ошибок
  if (error.response && error.response.status === 400) {
    if (error.response.data.detail){
      alert(error.response.data.detail);
    }else {
        return Promise.reject(error);
    }
  }
  if (error.response && error.response.status === 422) {
    console.log(error)
  }
  return Promise.reject(error);
});

// Экспорт конфигурированного экземпляра axios
export default axios;
