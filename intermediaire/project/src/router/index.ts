import { createRouter, createWebHistory } from 'vue-router';
import Home from '@/views/Home.vue';
import { useAuthStore } from '@/stores/auth';

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/parcelle/:id',
      name: 'parcelle-details',
      component: () => import('@/views/ParcelleDetails.vue'),
      props: true
    },
    {
      path: '/favoris',
      name: 'favoris',
      component: () => import('@/views/Favoris.vue'),
      meta: { requiresAuth: true }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('@/views/Login.vue')
    },
    {
      path: '/acheter',
      name: 'acheter',
      component: () => import('@/views/Home.vue')
    },
    {
      path: '/vendre',
      name: 'vendre',
      component: () => import('@/views/Home.vue')
    },
    {
      path: '/location',
      name: 'location',
      component: () => import('@/views/Home.vue')
    }
  ]
});

router.beforeEach((to, from, next) => {
  const authStore = useAuthStore();
  
  if (to.meta.requiresAuth && !authStore.isAuthenticated()) {
    next({ name: 'login', query: { redirect: to.fullPath } });
  } else {
    next();
  }
});

export default router;