import {createRouter, createWebHistory} from "vue-router"
import nav from "./views/nav.vue";
import blog from "./views/blog.vue";
import gist from "./views/gist.vue";
import article from "./views/article.vue";

const routes = [
    {path: '/', name: 'nav', component: nav},
    {path: '/blog', name: 'blog', component: blog},
    {path: '/gist', name: 'gist', component: gist},
    {path: '/article', name: 'article', component: article}
]


const router = createRouter({
    history: createWebHistory(),
    routes
})

export default router