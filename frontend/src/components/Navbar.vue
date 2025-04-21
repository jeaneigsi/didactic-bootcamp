<script setup lang="tsx">

import {ref} from "vue"

const menuOpen =ref(false)
const toggleMenu= ()=>{
    menuOpen.value = !menuOpen.value
}

</script>

<template>
<nav class="bg-blue-500 p-4 text-white flex justify-between items-center border-2">
    <!-- Logo 
     <router-link to="/">
        <img src="/logo.svg" alt="logo" class="h-1">
     </router-link>
   -->
     <!-- Menu  mobile-->

     <button @click="toggleMenu" class="md:hidden">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
      </svg>

     </button>

        <!-- Menu desktop-->
         <ul v-if="menuOpen" class="md:hidden bg-blue-500 text-white p-4 space-y-2">
            <li><router-link to="/">Home</router-link></li>
            <li><router-link to="/Achat">Achat</router-link></li>
            <li><router-link to="/Location">Location</router-link></li>

        </ul>

</nav>


</template>
<style scoped></style>