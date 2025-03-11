<script setup lang="ts">
import { Button } from '@/components/ui/button'
import { Input } from '@/components/ui/input'
</script>

<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-50">
    <div class="border rounded-lg shadow-lg p-6 w-full max-w-md bg-white">
      <div class="text-center">
        <h3 class="text-2xl font-semibold text-gray-800">Create Account</h3>
        <p class="mt-2 text-xs text-gray-600">
          By continuing, you agree to our <span class="font-medium text-blue-500">User Agreement</span> and acknowledge that you understand the <span class="font-medium text-blue-500">Privacy Policy</span>.
        </p>
      </div>

      <div class="mt-6 flex flex-col items-center gap-4">
        <div class="w-full">
          <Input
              type="email"
              placeholder="Enter your email"
              class="w-full"
              :class="inputClasses"
          />
        </div>

        <div class="w-full">
          <Input
              v-model="password"
              @input="passwordInput"
              placeholder="Enter your password"
              class="w-full"
              :class="inputClasses"
              type="password"
          />
        </div>

<!--        <div class="w-full text-center mt-4">-->
<!--          <p class="text-sm">-->
<!--            <RouterLink to="/forgot-password" class="text-blue-500 underline">Forgot password?</RouterLink>-->
<!--          </p>-->
<!--        </div>-->

        <div class="mt-6 flex flex-col items-center gap-4">
          <Button
              @click="handleLogin"
              class="w-full py-2 px-4 text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
          >
            Create Account
          </Button>

          <p class="text-sm text-gray-600">
            Already a suckers? <RouterLink to="/login" class="text-blue-500 underline">Log In</RouterLink>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>