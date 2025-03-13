import { defineStore } from 'pinia';
import { ref, computed } from 'vue';
import { useAuthStore } from './auth';
import type { Parcelle } from '@/types';

export const useParcellesStore = defineStore('parcelles', () => {
  const authStore = useAuthStore();
  const parcelles = ref<Parcelle[]>([]);
  const loading = ref(false);
  const error = ref<string | null>(null);
  const searchQuery = ref('');
  const selectedVille = ref<string | null>(null);
  const selectedCategorie = ref<string | null>(null);
  const priceRange = ref<[number, number]>([0, 1000000]);

  const fetchParcelles = async () => {
    try {
      loading.value = true;
      const response = await authStore.api.get('/parcelles/');
      parcelles.value = response.data;
    } catch (err) {
      error.value = "Erreur lors du chargement des parcelles";
      console.error(err);
    } finally {
      loading.value = false;
    }
  };

  const fetchParcelleById = async (id: number): Promise<Parcelle> => {
    const response = await authStore.api.get(`/parcelles/${id}/`);
    return response.data;
  };

  const addToFavorites = async (parcelleId: number) => {
    if (!authStore.isAuthenticated()) {
      error.value = "Veuillez vous connecter pour ajouter aux favoris";
      return;
    }
    try {
      await authStore.api.post('/favoris/', { parcelle: parcelleId });
      const parcelle = parcelles.value.find(p => p.id === parcelleId);
      if (parcelle) {
        parcelle.isFavorite = true;
      }
    } catch (err) {
      console.error('Erreur lors de l\'ajout aux favoris:', err);
    }
  };

  const removeFromFavorites = async (parcelleId: number) => {
    try {
      await authStore.api.delete(`/favoris/${parcelleId}/`);
      const parcelle = parcelles.value.find(p => p.id === parcelleId);
      if (parcelle) {
        parcelle.isFavorite = false;
      }
    } catch (err) {
      console.error('Erreur lors de la suppression des favoris:', err);
    }
  };

  const filteredParcelles = computed(() => {
    return parcelles.value.filter(parcelle => {
      const matchesSearch = parcelle.nom.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
                          parcelle.description.toLowerCase().includes(searchQuery.value.toLowerCase());
      const matchesVille = !selectedVille.value || parcelle.ville === selectedVille.value;
      const matchesCategorie = !selectedCategorie.value || parcelle.categorie === selectedCategorie.value;
      const matchesPrice = parcelle.prix >= priceRange.value[0] && parcelle.prix <= priceRange.value[1];
      
      return matchesSearch && matchesVille && matchesCategorie && matchesPrice;
    });
  });

  const predictProfitability = (parcelle: Parcelle) => {
    const prixAuM2 = parcelle.prix / parcelle.superficie;
    const moyennePrixVille = 5000;
    
    if (prixAuM2 < moyennePrixVille * 0.8) {
      return {
        score: 'Excellent',
        message: 'Prix très attractif par rapport au marché'
      };
    } else if (prixAuM2 < moyennePrixVille) {
      return {
        score: 'Bon',
        message: 'Prix légèrement en dessous du marché'
      };
    } else {
      return {
        score: 'Moyen',
        message: 'Prix conforme au marché'
      };
    }
  };

  return {
    parcelles,
    loading,
    error,
    searchQuery,
    selectedVille,
    selectedCategorie,
    priceRange,
    filteredParcelles,
    fetchParcelles,
    fetchParcelleById,
    addToFavorites,
    removeFromFavorites,
    predictProfitability
  };
});