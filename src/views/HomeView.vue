<script>
export default {
  data() {
    return {
      message: 'Hello App from script!',
      titleClass: 'title',
      count: 0,
    }
  },
  methods: {
    increment() {
      this.count++
    },

    inputForFname(e) {
      this.fname = e.target.value
    },
  },
}
</script>

<template>
  <button @click="increment">press to increment</button>
  <h1 :class="title">{{ count }}</h1>

  <a href="http://home"></a>
  <a href="http://about"></a>

  <input v-model="fname" placeholder="enter your fname here" @input="inputForFname" />
  <p>Input fname: {{ fname }}</p>
</template>

<style>
.title {
  color: red;
}
</style>
