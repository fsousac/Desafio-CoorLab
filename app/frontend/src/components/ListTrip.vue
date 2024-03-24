<template>
  <div>
    <h1>Listagem de Viagens</h1>
    <ul>
      <li v-for="viagem in viagens" :key="viagem.id">
        <p><strong>Nome da empresa:</strong> {{ viagem.name }}</p>
        <p><strong>Cidade de destino:</strong> {{ viagem.city }}</p>
        <p><strong>Preço (conforto):</strong> {{ viagem.price_confort }}</p>
        <p><strong>Preço (econômico):</strong> {{ viagem.price_econ }}</p>
        <p><strong>Duração:</strong> {{ viagem.duration }}</p>
        <p v-if="viagem.seat"><strong>Poltrona:</strong> {{ viagem.seat }}</p>
        <p v-if="viagem.bed"><strong>Leito:</strong> {{ viagem.bed }}</p>
      </li>
    </ul>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      viagens: []
    };
  },
  created() {
    this.listarViagens();
  },
  methods: {
    async listarViagens() {
      try {
        const response = await axios.get('http://localhost:3000/viagens/');
        this.viagens = response.data;
      } catch (error) {
        console.error('Erro ao listar viagens:', error);
      }
    }
  }
};
</script>

<style scoped>
/* Estilos específicos do componente */
</style>
