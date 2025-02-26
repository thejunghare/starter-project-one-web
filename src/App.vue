<script setup>
import headerComponent from './components/headerComponent.vue'
import { RouterLink, RouterView } from 'vue-router'
import { ref } from 'vue'

const emailAddress = ref('')
const password = ref('')

const passwordInput = (e) => {
  password.value = e.target.value
}

const emailAddressInput = (e) => {
  emailAddress.value = e.target.value
}

const handleLogin = () => {
  // Handle login logic here
  router.push('/dashboard')
}
</script>

<template>
  <headerComponent />
  <RouterView v-slot="{ Component }">
    <transition name="fade" mode="out-in">
      <component :is="Component" />
    </transition>
  </RouterView>

  <div v-if="$route.path === '/'" class="loginContainer">
    <div class="loginContainerHeader">
      <h3>Log In</h3>
      <p>
        By continuing, you agree to our User Agreement and acknowledge that you understand the
        Privacy Policy.
      </p>
    </div>
    <div class="loginContainerInput">
      <input
        v-model="emailAddress"
        @input="emailAddressInput"
        placeholder="Enter your email address"
      />
      <input v-model="password" @input="passwordInput" placeholder="Enter your password" />
    </div>
    <div class="loginContainerButtonPart">
      <button @click="handleLogin">Login</button>
      <p><RouterLink to="/forgot-password">Forgot password?</RouterLink></p>
      <p>New to suckers? <RouterLink to="/create-account">Create account</RouterLink></p>
    </div>
  </div>
</template>

<style>
body {
  box-sizing: border-box;
  overflow: hidden;
}

.loginContainer {
  border: 2px solid #f2f2f2;
  width: 50vw;
  height: 90vh;
  margin: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
}

.loginContainerHeader {
  width: 50%;
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}

.loginContainerInput {
  width: 50%;
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}

.loginContainerInput > input {
  margin-bottom: 10px;
  padding: 12px;
  border-radius: 8px;
  outline: none;
  border: none;
  background-color: #f2f2f2;
}

.loginContainerButtonPart {
  width: 25%;
  display: flex;
  flex-direction: column;
  margin-bottom: 10px;
}

.loginContainerButtonPart > button {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 10px;
  border: none;
  border-radius: 8px;
  padding: 10px;
  cursor: pointer;
  background-color: blueviolet;
  font-weight: bold;
  color: white;
}

.loginContainerButtonPart > p {
  text-align: center;
}
</style>
