/* eslint-disable import/order */
import '@/@iconify/icons-bundle'
import App from '@/App.vue'
import vuetify from '@/plugins/vuetify'
import { loadFonts } from '@/plugins/webfontloader'
import router from '@/router'
import axios, { type AxiosInstance } from 'axios'
import '@core/scss/template/index.scss'
import '@layouts/styles/index.scss'
import '@styles/styles.scss'
import { createPinia } from 'pinia'
import { createApp } from 'vue'


declare module '@vue/runtime-core' {
    interface ComponentCustomProperties {
      $axios: AxiosInstance;
    }
  }

loadFonts()

// Create vue app
const app = createApp(App);

axios.defaults.baseURL = 'http://127.0.0.1:8000/';
app.config.globalProperties.$axios = axios;

// Use plugins
app.use(vuetify)
app.use(createPinia())
app.use(router)

// Mount vue app
app.mount('#app')
