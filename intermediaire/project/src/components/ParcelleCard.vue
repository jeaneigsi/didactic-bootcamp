<template>
  <div class="bg-white rounded-lg shadow-md overflow-hidden">
    <div class="relative">
      <img :src="parcelle.image" :alt="parcelle.nom" class="w-full h-48 object-cover" />
      <div class="absolute top-2 left-2 bg-green-500 text-white px-2 py-1 rounded-md text-sm">
        Vérifié par agenz
      </div>
    </div>
    
    <div class="p-4">
      <div class="flex justify-between items-start mb-2">
        <h2 class="text-xl font-bold text-gray-900">{{ formatPrice(parcelle.prix) }} DH</h2>
        <button @click="toggleFavorite" class="text-gray-400 hover:text-red-500">
          <HeartIcon class="h-6 w-6" :class="{ 'text-red-500': parcelle.isFavorite }" />
        </button>
      </div>
      
      <p class="text-gray-600 mb-2">{{ parcelle.nom }}</p>
      
      <div class="flex items-center gap-4 text-sm text-gray-500 mb-4">
        <span>{{ parcelle.superficie }} m²</span>
        <span>{{ parcelle.ville }}</span>
      </div>
      
      <div class="flex justify-between items-center">
        <router-link 
          :to="{ name: 'parcelle-details', params: { id: parcelle.id }}"
          class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
        >
          Voir détails
        </router-link>
        <button 
          @click="showPrediction"
          class="px-4 py-2 border border-blue-600 text-blue-600 rounded-lg hover:bg-blue-50"
        >
          Prédiction
        </button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { HeartIcon } from '@heroicons/vue/24/outline';
import { useParcellesStore } from '@/stores/parcelles';
import type { Parcelle } from '@/types';

const props = defineProps<{
  parcelle: Parcelle;
}>();

const parcellesStore = useParcellesStore();

const toggleFavorite = () => {
  if (props.parcelle.isFavorite) {
    parcellesStore.removeFromFavorites(props.parcelle.id);
  } else {
    parcellesStore.addToFavorites(props.parcelle.id);
  }
};

const formatPrice = (price: number) => {
  return price.toLocaleString('fr-FR');
};

const showPrediction = () => {
  const prediction = parcellesStore.predictProfitability(props.parcelle);
  alert(`Score: ${prediction.score}\n${prediction.message}`);
};
</script>