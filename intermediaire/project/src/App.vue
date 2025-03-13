<template>
  <div class="min-h-screen bg-gray-50">
    <!-- Header -->
    <header class="bg-white shadow-sm">
      <nav class="container mx-auto px-4 py-4 flex items-center justify-between">
        <div class="flex items-center space-x-8">
          <router-link to="/" class="flex items-center space-x-2">
            <img src="C:\Users\jean\Documents\Bootcamp-django\projet\didactic-bootcamp\intermediaire\project\src\assets\vue.svg" alt="Logo" class="h-8 w-8" />
            <span class="text-xl font-bold text-blue-600">ParcellesApp</span>
          </router-link>
          <div class="hidden md:flex space-x-6">
            <router-link to="/acheter" class="text-gray-700 hover:text-blue-600">Acheter</router-link>
            <router-link to="/vendre" class="text-gray-700 hover:text-blue-600">Vendre</router-link>
            <router-link to="/location" class="text-gray-700 hover:text-blue-600">Location</router-link>
          </div>
        </div>
        <div class="flex items-center space-x-4">
          <button v-if="!isAuthenticated" @click="login" class="text-blue-600 hover:text-blue-700">
            Se connecter
          </button>
          <button v-if="!isAuthenticated" @click="register" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
            S'inscrire
          </button>
          <div v-else class="flex items-center space-x-4">
            <router-link to="/favoris" class="text-gray-700 hover:text-blue-600">
              <HeartIcon class="h-6 w-6" />
            </router-link>
            <router-link to="/panier" class="text-gray-700 hover:text-blue-600">
              <ShoppingCartIcon class="h-6 w-6" />
            </router-link>
            <button @click="logout" class="text-gray-700 hover:text-red-600">
              Déconnexion
            </button>
          </div>
        </div>
      </nav>
    </header>

    <!-- Search Bar -->
    <div class="bg-white border-b">
      <div class="container mx-auto px-4 py-4">
        <div class="flex flex-col md:flex-row gap-4">
          <div class="flex-1">
            <input 
              type="text" 
              placeholder="Entrez une ville, un quartier, une adresse"
              class="w-full px-4 py-2 border rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
            />
          </div>
          <div class="flex gap-2">
            <select class="px-4 py-2 border rounded-lg bg-white">
              <option>Prix</option>
              <option>0 - 500,000 DH</option>
              <option>500,000 - 1M DH</option>
              <option>1M+ DH</option>
            </select>
            <select class="px-4 py-2 border rounded-lg bg-white">
              <option>Type</option>
              <option>Résidentiel</option>
              <option>Commercial</option>
              <option>Agricole</option>
            </select>
            <button class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700">
              Rechercher
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <main class="container mx-auto px-4 py-8">
      <router-view></router-view>
    </main>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { HeartIcon, ShoppingCartIcon } from '@heroicons/vue/24/outline'

const isAuthenticated = ref(false)

const login = () => {
  // Implémenter la logique de connexion
}

const register = () => {
  // Implémenter la logique d'inscription
}

const logout = () => {
  // Implémenter la logique de déconnexion
}
</script>