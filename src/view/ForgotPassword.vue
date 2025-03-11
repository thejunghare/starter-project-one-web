<template>
  <div class="flex items-center justify-center min-h-screen bg-gray-50">
    <div class="border rounded-lg shadow-lg p-6 w-full max-w-md bg-white">
      <div class="text-center">
        <h3 class="text-2xl font-semibold text-gray-800">Forgot Password</h3>
        <p class="mt-2 text-xs text-gray-600">
          Enter your email to receive a password reset link.
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

        <div class="mt-6 w-full text-center">
          <Button
              @click="handleResetPassword"
              class="w-full py-2 px-4 text-white bg-blue-600 rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50"
          >
            Reset Password
          </Button>
        </div>

        <div class="mt-4 text-sm text-center">
          <p class="text-gray-600">
            Remember your password? <RouterLink to="/login" class="text-blue-500 underline">Log In</RouterLink>
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      email: ''
    };
  },
  computed: {
    inputClasses() {
      return 'px-4 py-2 border rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 focus:ring-opacity-50 text-sm w-full';
    }
  },
  methods: {
    handleResetPassword() {
      // handle password reset logic here
    }
  }
};
</script>

<style scoped>
/* You can add custom styles here if needed */
</style>
