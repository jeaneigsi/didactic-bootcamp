import { createWebHistory,createRouter } from "vue-router";

import Home from "../pages/Home.vue";
import Achat from "../pages/Achat.vue";
import Location from "../pages/Location.vue";
import NotFound from "../pages/NotFound.vue";

const routes=[
    {
        "path":"/","component":Home
    }
    ,{
        "path":"/achat","component":Achat
    }
    ,{
        "path":"/location","component":Location
    }
    ,{"path":"/:pathMatch(.*)*","component":NotFound}
]

const router = createRouter({
    history: createWebHistory(),
    routes,
  });
  
  export default router;
  