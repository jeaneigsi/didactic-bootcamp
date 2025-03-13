import { defineStore } from 'pinia';
import { ref } from 'vue';
import axios from 'axios';
import type { User, AuthResponse } from '@/types';

export const useAuthStore = defineStore('auth', () => {
  const user = ref<User | null>(null);
  const token = ref<string | null>(localStorage.getItem('token'));

  const api = axios.create({
    baseURL: 'http://localhost:8000',
    headers: {
      'Content-Type': 'application/json'
    }
  });

  api.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Token ${token}`;
    }
    return config;
  });

  api.interceptors.response.use(
    (response) => response,
    (error) => {
      if (error.response?.status === 401) {
        logout();
      }
      return Promise.reject(error);
    }
  );

  const login = async (email: string, password: string): Promise<boolean> => {
    try {
      const response = await api.post<AuthResponse>('/api/api-token-auth/', {
        username: email,
        password,
      });
      
      token.value = response.data.token;
      localStorage.setItem('token', response.data.token);
      
      const userResponse = await api.get('/api/users/me/');
      user.value = userResponse.data;
      
      return true;
    } catch (error) {
      console.error('Erreur de connexion:', error);
      return false;
    }
  };

  const logout = () => {
    user.value = null;
    token.value = null;
    localStorage.removeItem('token');
  };

  const isAuthenticated = (): boolean => {
    return !!token.value;
  };

  return {
    user,
    token,
    login,
    logout,
    isAuthenticated,
    api,
  };
});