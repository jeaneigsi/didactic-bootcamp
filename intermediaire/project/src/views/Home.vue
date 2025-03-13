<template>
  <div>
    <SearchFilters />
    
    <div class="container mx-auto px-4 py-8">
      <h1 class="text-2xl font-bold mb-6">Parcelles disponibles</h1>
      
      <div v-if="parcellesStore.loading" class="text-center py-8">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
      </div>
      
      <div v-else-if="parcellesStore.error" class="text-center py-8 text-red-600">
        {{ parcellesStore.error }}
      </div>
      
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <ParcelleCard 
          v-for="parcelle in parcellesStore.filteredParcelles" 
          :key="parcelle.id" 
          :parcelle="parcelle"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue';
import { useParcellesStore } from '@/stores/parcelles';
import ParcelleCard from '@/components/ParcelleCard.vue';
import SearchFilters from '@/components/SearchFilters.vue';

const parcellesStore = useParcellesStore();

onMounted(() => {
  parcellesStore.fetchParcelles();
});
</script>