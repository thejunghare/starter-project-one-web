import { createApp } from 'vue'
import '../src/assets/index.css'
import App from './App.vue'
// import router from '../src/router/index'
import router from './router'

createApp(App).use(router).mount('#app')