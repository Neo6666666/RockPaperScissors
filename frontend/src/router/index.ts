import { createRouter, createWebHistory } from 'vue-router'

import { store } from '@/store'

import Home from '@/pages/Home'
import Login from '@/pages/Login'
import Register from '@/pages/Register'
import NotFound from '@/pages/NotFound'

export enum RouteNames {
  Login = 'Login',
  Register = 'Register',
  Home = 'Home'
}

const routes = [
  {
    path: '/',
    name: RouteNames.Home,
    component: Home,
    meta: {
      title: 'Home',
      requiresAuth: true
    },
  },
  {
    path: '/login',
    name: RouteNames.Login,
    component: Login,
    meta: {
      title: 'Login',
    },
  },
  {
    path: '/register',
    name: RouteNames.Register,
    component: Register,
    meta: {
      title: 'Register',
    },
  },
  { path: '/:pathMatch(.*)*', name: 'not-found', component: NotFound },
  // if you omit the last `*`, the `/` character in params will be encoded when resolving or pushing
  { path: '/:pathMatch(.*)', name: 'bad-not-found', component: NotFound },
]

const router = createRouter({
  history: createWebHistory(),
  routes,
})

router.beforeEach((to, from, next) => {
  const isLoggedIn = store.getters.isLoggedIn
  const isAuthRoute = to.name === RouteNames.Login || to.name === RouteNames.Register

  console.log(to, isLoggedIn)

  if (isLoggedIn && isAuthRoute) {
    next({ name: RouteNames.Home })
  } else {
    if (!isLoggedIn && to.matched.some((record) => record.meta.requiresAuth)) {
      next({ name: RouteNames.Login })
    } else {
      next()
    }
  }
})

export default router
