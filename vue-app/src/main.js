import {createApp} from 'vue'
import ElementPlus from 'element-plus';
import 'element-plus/lib/theme-chalk/index.css';
import router from "./router";
import './index.css'
import App from './App.vue';
import Markdown from 'vue3-markdown-it';
import 'highlight.js/styles/monokai.css';


const app = createApp(App);

app
    .use(Markdown)
    .use(router)
    .use(ElementPlus)
    .mount('#app')

app.config.globalProperties.$apiUrl = 'http://53th.cn:3000';
