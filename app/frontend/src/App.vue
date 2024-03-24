<template>
  <div class="barra-lateral">
    <router-link to="/add-trip">
      <img
        src="./assets/add.png"
        alt="add"
        class="icone"
        title="Adicionar viagem"
      />
    </router-link>
    <router-link to="/list-trip">
      <img
        src="./assets/search.png"
        alt="search"
        class="icone"
        title="Pesquisar viagens"
      />
    </router-link>
  </div>
  <img alt="logo" src="./assets/logo.png" class="logo" />
  <router-view />
</template>

<script>
import router from "./router/index";
// import AddTrip from "./components/AddTrip.vue";
// import ListTrip from "./components/ListTrip.vue";
import { createApp } from "vue";

export default {
  name: "App",
  setup() {
    const app = createApp({});
    app.use(router);
    return {};
  },
  components: {
    // AddTrip,
    // ListTrip,
  },
};
</script>

<style>
@import "./styles.css";
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
