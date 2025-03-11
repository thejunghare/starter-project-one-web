<script setup>
import { RouterLink, RouterView } from 'vue-router';
import { ref } from 'vue';
import {
  DropdownMenu,
  DropdownMenuContent,
  DropdownMenuItem,
  DropdownMenuTrigger,
} from '@/components/ui/dropdown-menu';
import { Button } from '@/components/ui/button';
import { Bars3Icon } from '@heroicons/vue/24/solid';

const isMenuOpen = ref(false);
const toggleMenu = () => {
  isMenuOpen.value = !isMenuOpen.value;
};
</script>

<template>
  <header class="bg-gradient-to-r from-pink-500 to-yellow-400 shadow-md py-4">
    <div class="max-w-7xl mx-auto px-6 flex justify-between items-center">
      <!-- Logo -->
      <RouterLink to="/" class="text-3xl font-bold text-white">SwipeMatch</RouterLink>
      
      <!-- Desktop Navigation -->
      <nav class="hidden md:flex space-x-6 text-white font-semibold">
        <RouterLink to="/" class="hover:underline">Home</RouterLink>
        <RouterLink to="/profile" class="hover:underline">Profile</RouterLink>
        <RouterLink to="/messages" class="hover:underline">Messages</RouterLink>
        <RouterLink to="/notifications" class="hover:underline">Notifications</RouterLink>
      </nav>
      
      <!-- User Avatar & Dropdown -->
      <div class="flex items-center space-x-4">
        <RouterLink to="/profile">
          <img src="https://via.placeholder.com/40" alt="User Avatar" class="rounded-full h-10 w-10 object-cover border-2 border-white shadow-md" />
        </RouterLink>
        
        <DropdownMenu>
          <DropdownMenuTrigger>
            <Button variant="outline" class="text-white border-white">More</Button>
          </DropdownMenuTrigger>
          <DropdownMenuContent class="w-48 bg-white shadow-md rounded-lg">
            <DropdownMenuItem>
              <RouterLink to="/settings" class="block p-2 text-gray-700 hover:bg-gray-100 rounded">Settings</RouterLink>
            </DropdownMenuItem>
            <DropdownMenuItem>
              <RouterLink to="/logout" class="block p-2 text-gray-700 hover:bg-gray-100 rounded">Log Out</RouterLink>
            </DropdownMenuItem>
          </DropdownMenuContent>
        </DropdownMenu>
      </div>
      
      <!-- Mobile Menu Button -->
      <div class="md:hidden flex items-center">
        <Button @click="toggleMenu" class="text-white">
          <Bars3Icon class="h-6 w-6" />
        </Button>
      </div>
    </div>
    
    <!-- Mobile Menu -->
    <div v-if="isMenuOpen" class="md:hidden flex flex-col bg-white shadow-md py-4 mt-2 text-gray-700">
      <RouterLink to="/" class="px-6 py-2 hover:bg-gray-100">Home</RouterLink>
      <RouterLink to="/profile" class="px-6 py-2 hover:bg-gray-100">Profile</RouterLink>
      <RouterLink to="/messages" class="px-6 py-2 hover:bg-gray-100">Messages</RouterLink>
      <RouterLink to="/notifications" class="px-6 py-2 hover:bg-gray-100">Notifications</RouterLink>
      <RouterLink to="/settings" class="px-6 py-2 hover:bg-gray-100">Settings</RouterLink>
      <RouterLink to="/logout" class="px-6 py-2 hover:bg-gray-100">Log Out</RouterLink>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
button:active {
  transform: scale(0.95);
}
</style>
