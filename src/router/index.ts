import { createRouter, createWebHistory } from 'vue-router'
import Login from '@/view/Login.vue'
import Home from '@/view/Home.vue'
import CreateAccount from '@/view/CreateAccount.vue'
import ForgotPassword from '@/view/ForgotPassword.vue'
import ProfileSetUp from '@/view/ProfileSetUp.vue'
import Dashboard from '@/view/DashboardView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/create-account',
      name: 'create-account',
      component: CreateAccount
    },
    {
      path: '/forgot-password',
      name: 'forgot-password',
      component: ForgotPassword
    },
    {
      path: '/profile-setup',
      name: 'profile-setup',
      component: ProfileSetUp
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard
    }
  ]
})

export default router