<script setup>
import { ref, computed } from 'vue';

const cards = [
    { id: 1, name: 'John', bio: 'Love to travel and code!', image: 'https://randomuser.me/api/portraits/men/1.jpg' },
    { id: 2, name: 'Emma', bio: 'Coffee lover & photographer', image: 'https://randomuser.me/api/portraits/women/1.jpg' },
    { id: 3, name: 'Lucas', bio: 'Sports and fitness enthusiast', image: 'https://randomuser.me/api/portraits/men/2.jpg' }
];

const currentIndex = ref(0);
const startX = ref(0);
const deltaX = ref(0);
const isSwiping = ref(false);

const startSwipe = (e) => {
    isSwiping.value = true;
    startX.value = e.clientX || e.touches[0].clientX;
};

const onSwipeMove = (e) => {
    if (!isSwiping.value) return;
    const currentX = e.clientX || e.touches[0].clientX;
    deltaX.value = currentX - startX.value;
};

const endSwipe = () => {
    isSwiping.value = false;
    const threshold = 100;
    if (deltaX.value > threshold && currentIndex.value > 0) {
        currentIndex.value--;
    } else if (deltaX.value < -threshold && currentIndex.value < cards.length - 1) {
        currentIndex.value++;
    }
    deltaX.value = 0;
};

const getCardStyle = computed(() => (index) => {
    if (index < currentIndex.value) {
        return { transform: 'translateX(-120%) rotate(-10deg)', opacity: 0 };
    } else if (index === currentIndex.value) {
        return {
            transform: `translateX(${deltaX.value}px) rotate(${deltaX.value / 20}deg)`,
            transition: isSwiping.value ? 'none' : 'transform 0.3s ease-in-out',
        };
    } else {
        return { transform: 'translateX(120%) rotate(10deg)', opacity: 0 };
    }
});
</script>

<template>
    <div class="flex justify-center items-center h-screen bg-gradient-to-br from-pink-500 to-yellow-400">
        <div class="relative w-80 h-[500px] overflow-hidden">
            <div v-for="(card, index) in cards" :key="index" 
                class="absolute w-full h-full bg-white shadow-lg rounded-2xl flex flex-col items-center justify-center p-6 transition-transform duration-300"
                :style="getCardStyle(index)" 
                @mousedown="startSwipe" @mousemove="onSwipeMove" @mouseup="endSwipe" @mouseleave="endSwipe"
                @touchstart="startSwipe" @touchmove="onSwipeMove" @touchend="endSwipe">
                <div class="w-32 h-32 rounded-full overflow-hidden shadow-md border-4 border-white mb-4">
                    <img :src="card.image" alt="Profile Image" class="w-full h-full object-cover" />
                </div>
                <h3 class="text-2xl font-bold text-gray-800">{{ card.name }}</h3>
                <p class="text-gray-600 text-center mt-2">{{ card.bio }}</p>
                <div class="absolute bottom-6 flex gap-6">
                    <button class="bg-red-500 text-white px-6 py-3 rounded-full text-xl shadow-md active:scale-90 transition"
                        @click="currentIndex = Math.min(currentIndex + 1, cards.length - 1)">
                        ❌
                    </button>
                    <button class="bg-green-500 text-white px-6 py-3 rounded-full text-xl shadow-md active:scale-90 transition"
                        @click="currentIndex = Math.min(currentIndex + 1, cards.length - 1)">
                        ❤️
                    </button>
                </div>
            </div>
        </div>
    </div>
</template>

<style scoped>
button:active {
    transform: scale(0.9);
}
</style>
