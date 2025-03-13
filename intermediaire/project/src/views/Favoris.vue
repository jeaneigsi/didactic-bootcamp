<template>
  <div class="container mx-auto px-4 py-8">
    <h1 class="text-2xl font-bold mb-6">Mes Favoris</h1>
    
    <div v-if="loading" class="text-center py-8">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-600 mx-auto"></div>
    </div>
    
    <div v-else-if="error" class="text-center py-8 text-red-600">
      {{ error }}
    </div>
    
    <div v-else-if="favoris.length === 0" class="text-center py-8 text-gray-600">
      Vous n'avez pas encore de favoris
    </div>
    
    <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
      <ParcelleCard 
        v-for="parcelle in favoris" 
        :key="parcelle.id" 
        :parcelle="parcelle"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue';
import { useAuthStore } from '@/stores/auth';
import ParcelleCard from '@/components/ParcelleCard.vue';
import type { Parcelle } from '@/types';

const authStore = useAuthStore();
const favoris = ref<Parcelle[]>([]);
const loading = ref(true);
const error = ref<string | null>(null);

onMounted(async () => {
  try {
    const response = await authStore.api.get('/favoris/');
    favoris.value = response.data.map((favori: any) => favori.parcelle);
  } catch (err) {
    error.value = "Erreur lors du chargement des favoris";
    console.error(err);
  } finally {
    loading.value = false;
  }
});
</script>