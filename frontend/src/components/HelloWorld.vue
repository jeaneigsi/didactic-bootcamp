<script setup lang="ts">
import { ref } from 'vue';

const cards = ref([
  {
    title: 'Immobilier Neuf',
    description: 'Découvrez nos offres exclusives à Casablanca',
    image: 'path/to/image1.jpg',
  },
  {
    title: 'Appartement',
    description: 'à vendre',
    image: 'path/to/image2.jpg',
  },
  {
    title: 'Villa',
    description: 'à vendre',
    image: 'path/to/image3.jpg',
  },
  {
    title: 'Villas de Luxe',
    description: 'à Casablanca',
    image: 'path/to/image4.jpg',
  },
  {
    title: 'Investir dans un Studio',
    description: 'avec Agenz',
    image: 'path/to/image5.jpg',
  },
  {
    title: 'Vous vendez ?',
    description: 'Estimez votre bien en 2 min',
    image: 'path/to/image6.jpg',
  },
]);
</script>

<template>
  <div id="app" class="font-sans">
    <header class="bg-white p-4 border-b border-gray-200">
      <nav class="flex justify-between items-center">
        <ul class="flex space-x-4">
          <li><a href="#" class="text-black">Acheter</a></li>
          <li><a href="#" class="text-black">Vendre</a></li>
          <li><a href="#" class="text-black">Crédit immobilier</a></li>
          <li><a href="#" class="text-black">Prix immobilier</a></li>
          <li><a href="#" class="text-black">Location</a></li>
          <li><a href="#" class="text-black">Carrières</a></li>
        </ul>
        <div class="flex space-x-4">
          <button class="bg-gray-200 text-black px-4 py-2">Français</button>
          <button class="bg-purple-600 text-white px-4 py-2">Estimez votre bien</button>
          <button class="bg-gray-200 text-black px-4 py-2">Se connecter</button>
        </div>
      </nav>
    </header>
    <main class="p-4">
      <section class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div v-for="card in cards" :key="card.title" class="bg-white border border-gray-200 rounded-lg shadow">
          <img :src="card.image" :alt="card.title" class="w-full h-48 object-cover rounded-t-lg">
          <div class="p-4">
            <h2 class="text-xl font-semibold">{{ card.title }}</h2>
            <p class="text-gray-600">{{ card.description }}</p>
          </div>
        </div>
      </section>
    </main>
  </div>
</template>

<style scoped>
/* Ajoutez des styles personnalisés ici si nécessaire */
</style>