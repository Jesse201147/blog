import {createRouter,createWebHistory} from "vue-router"
import nav from "./views/nav.vue";
import blog from "./views/blog.vue";

const routes = [
    { path: '/',name: 'nav', component: nav },
    { path: '/blog', name: 'blog', component: blog },
]


const router =  createRouter({
    history: createWebHistory(),
    routes
})

export default router