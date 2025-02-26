import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import CreateAccountView from '../views/CreateAccountView.vue'
import ForgotPasswordView from '../views/ForgotPasswordView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView,
    },
    {
      path: '/forgot-password',
      name: 'forgot',
      component: ForgotPasswordView,
    },
    {
      path: '/create-account',
      // name: 'SignUp',
      component: CreateAccountView,
    },
  ],
})

export default router
