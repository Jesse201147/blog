import {createApp} from 'vue'
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import App from './App.vue';
import router from "./router";
import './index.css'

let app = createApp(App)

app
    .use(router)
    .use(ElementPlus)
    .mount('#app')

app.config.globalProperties.$apiUrl = 'http://53th.cn:3000';
