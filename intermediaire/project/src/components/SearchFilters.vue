<template>
  <div class="bg-white border-b">
    <div class="container mx-auto px-4 py-4">
      <div class="flex flex-col md:flex-row gap-4">
        <div class="flex-1">
          <input 
            v-model="parcellesStore.searchQuery"
            type="text" 
            placeholder="Entrez une ville, un quartier, une adresse"
            class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
          />
        </div>
        <div class="flex gap-2">
          <select 
            v-model="parcellesStore.selectedCategorie"
            class="px-4 py-2 border rounded-lg bg-white"
          >
            <option value="">Type</option>
            <option value="Residentiel">Résidentiel</option>
            <option value="Commercial">Commercial</option>
            <option value="Agricole">Agricole</option>
          </select>
          <select 
            v-model="parcellesStore.selectedVille"
            class="px-4 py-2 border rounded-lg bg-white"
          >
            <option value="">Ville</option>
            <option v-for="ville in villes" :key="ville" :value="ville">
              {{ ville }}
            </option>
          </select>
          <button 
            @click="parcellesStore.fetchParcelles()"
            class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700"
          >
            Rechercher
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue';
import { useParcellesStore } from '@/stores/parcelles';

const parcellesStore = useParcellesStore();
const villes = ref(['Dakar', 'Abidjan', 'Casablanca', 'Fès']);
</script>