import { createRouter, createWebHistory } from "vue-router";
import AddTrip from "../components/AddTrip.vue";
import ListTrip from "../components/ListTrip.vue";

const routes = [
  {
    path: "/",
    redirect: "/add-trip",
  },
  {
    path: "/add-trip",
    name: "AddTrip",
    component: AddTrip,
  },
  {
    path: "/list-trip",
    name: "ListTrip",
    component: ListTrip,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
