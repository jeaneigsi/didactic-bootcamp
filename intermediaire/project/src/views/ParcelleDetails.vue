<template>
  <div class="container mx-auto px-4 py-8">
    <div v-if="loading" class="text-center">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
    </div>
    
    <div v-else-if="error" class="text-center text-red-600">
      {{ error }}
    </div>
    
    <div v-else-if="parcelle" class="bg-white rounded-lg shadow-lg overflow-hidden">
      <div class="relative">
        <img :src="parcelle.image" :alt="parcelle.nom" class="w-full h-96 object-cover" />
        <div class="absolute top-4 left-4 bg-green-500 text-white px-3 py-1 rounded-md">
          Vérifié par agenz
        </div>
      </div>
      
      <div class="p-6">
        <div class="flex justify-between items-start mb-4">
          <h1 class="text-3xl font-bold text-gray-900">{{ parcelle.nom }}</h1>
          <div class="text-2xl font-bold text-blue-600">
            {{ formatPrice(parcelle.prix) }} DH
          </div>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
          <div>
            <h2 class="text-lg font-semibold mb-2">Détails</h2>
            <ul class="space-y-2">
              <li class="flex items-center">
                <span class="text-gray-600">Superficie:</span>
                <span class="ml-2 font-medium">{{ parcelle.superficie }} m²</span>
              </li>
              <li class="flex items-center">
                <span class="text-gray-600">Ville:</span>
                <span class="ml-2 font-medium">{{ parcelle.ville }}</span>
              </li>
              <li class="flex items-center">
                <span class="text-gray-600">Catégorie:</span>
                <span class="ml-2 font-medium">{{ parcelle.categorie }}</span>
              </li>
            </ul>
          </div>
          
          <div>
            <h2 class="text-lg font-semibold mb-2">Description</h2>
            <p class="text-gray-600">{{ parcelle.description }}</p>
          </div>
        </div>
        
        <div class="flex justify-between items-center">
          <button 
            @click="toggleFavorite" 
            class="flex items-center px-4 py-2 border rounded-lg"
            :class="parcelle.isFavorite ? 'border-red-500 text-red-500' : 'border-gray-300 text-gray-600'"
          >
            <HeartIcon class="h-5 w-5 mr-2" :class="{ 'text-red-500': parcelle.isFavorite }" />
            {{ parcelle.isFavorite ? 'Retirer des favoris' : 'Ajouter aux favoris' }}
          </button>
          
          <button 
            @click="showPrediction"
            class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Voir la prédiction
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { HeartIcon } from '@heroicons/vue/24/outline';
import { useParcellesStore } from '@/stores/parcelles';
import type { Parcelle } from '@/types';

const route = useRoute();
const parcellesStore = useParcellesStore();

const parcelle = ref<Parcelle | null>(null);
const loading = ref(true);
const error = ref<string | null>(null);

const formatPrice = (price: number) => {
  return price.toLocaleString('fr-FR');
};

const toggleFavorite = () => {
  if (!parcelle.value) return;
  
  if (parcelle.value.isFavorite) {
    parcellesStore.removeFromFavorites(parcelle.value.id);
  } else {
    parcellesStore.addToFavorites(parcelle.value.id);
  }
};

const showPrediction = () => {
  if (!parcelle.value) return;
  
  const prediction = parcellesStore.predictProfitability(parcelle.value);
  alert(`Score: ${prediction.score}\n${prediction.message}`);
};

onMounted(async () => {
  try {
    const id = parseInt(route.params.id as string);
    const response = await parcellesStore.fetchParcelleById(id);
    parcelle.value = response;
  } catch (err) {
    error.value = "Erreur lors du chargement de la parcelle";
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>