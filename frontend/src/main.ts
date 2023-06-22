import { createApp } from 'vue';
import App from './App.vue';
import { router } from './router';
import axios, { type AxiosInstance } from 'axios'
import vuetify from './plugins/vuetify';
import '@/scss/style.scss';
import PerfectScrollbar from 'vue3-perfect-scrollbar';
import VueApexCharts from 'vue3-apexcharts';
import VueTablerIcons from 'vue-tabler-icons';
import Maska from 'maska';
declare module '@vue/runtime-core' {
    interface ComponentCustomProperties {
      $axios: AxiosInstance;
    }
  }
const app = createApp(App);
axios.defaults.baseURL = 'http://127.0.0.0:8000';
app.config.globalProperties.$axios = axios;

app.use(router);
app.use(PerfectScrollbar);
app.use(VueTablerIcons);
app.use(Maska);
app.use(VueApexCharts);
app.use(vuetify).mount('#app');
