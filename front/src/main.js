import Vue from 'vue'
import ElementUI from 'element-ui'
import 'element-ui/lib/theme-chalk/index.css'
import App from './App.vue'

import VueRouter from 'vue-router'
import Vuex from 'vuex'

Vue.config.productionTip = false

import Index from './components/Index.vue'
import Login from './components/Login.vue'
import Register from './components/Register.vue'

Vue.use(ElementUI)
Vue.use(VueRouter)
Vue.use(Vuex)

const router = new VueRouter({
    routes: [{
            name: 'index',
            path: '/',
            component: Index,
            meta: {
                title: '首页'
            }
        },
        {
            name: 'login',
            path: '/login',
            component: Login,
            meta: {
                title: '登陆'
            }
        },
        {
            name: 'register',
            path: '/register',
            component: Register,
            meta: {
                title: '注册'
            }
        }
    ]
})

router.beforeEach((to, from, next) => {
    /* 路由发生变化修改页面title */
    if (to.meta.title) {
        document.title = to.meta.title
    }
    next()
})

const store = new Vuex.Store({
    state: {
    },
    mutations: {
    }
})

new Vue({
    router,
    store,
    render: h => h(App),
}).$mount('#app')
