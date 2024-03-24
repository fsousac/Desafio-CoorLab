<template>
  <div>
    <h1>Adicionar Nova Viagem</h1>
    <form @submit.prevent="adicionarViagem">
      <div>
        <label for="nome">Nome da Empresa:</label>
        <input type="text" id="nome" v-model="novaViagem.name" required />
      </div>
      <div>
        <label for="precoConforto">Preço (Conforto):</label>
        <input
          type="text"
          id="precoConforto"
          v-model="novaViagem.price_confort"
          required
          @blur="formatarPreco($event.target.value)"
        />
      </div>
      <div>
        <label for="precoEconomico">Preço (Econômico):</label>
        <input
          type="text"
          id="precoEconomico"
          v-model="novaViagem.price_econ"
          required
          @blur="formatarPreco($event.target.value)"
        />
      </div>
      <div>
        <label for="cidade">Cidade de Destino:</label>
        <input type="text" id="cidade" v-model="novaViagem.city" required />
      </div>
      <div>
        <label for="duracao">Duração:</label>
        <input
          type="text"
          id="duracao"
          v-model="novaViagem.duration"
          required
        />
      </div>
      <div>
        <label for="poltrona">Poltrona:</label>
        <input type="text" id="poltrona" v-model="novaViagem.seat" />
      </div>
      <div>
        <label for="leito">Leito:</label>
        <input type="text" id="leito" v-model="novaViagem.bed" />
      </div>
      <button type="submit">Adicionar Viagem</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      novaViagem: {
        id: 1,
        name: "",
        price_confort: "",
        price_econ: "",
        city: "",
        duration: "",
        seat: "",
        bed: "",
      },
    };
  },
  methods: {
    async adicionarViagem() {
      try {
        await axios.post(
          "http://localhost:3000/salvar-viagem/",
          Array(this.novaViagem)
        );
        alert("Viagem adicionada com sucesso!");
        // Limpar o formulário após a adição da viagem
        this.novaViagem = {
          name: "",
          price_confort: "",
          price_econ: "",
          city: "",
          duration: "",
          seat: "",
          bed: "",
        };
      } catch (error) {
        console.error("Erro ao adicionar viagem:", error);
        alert(
          "Erro ao adicionar viagem. Verifique o console para mais detalhes."
        );
      }
    },
    formatarPreco(inputValue) {
      // Remove todas as vírgulas
      numericValue = inputValue.replace(/[^\d,.]/g, "");
      numericValue = numericValue.replace(/\./g, ",");
      const hasComma = numericValue.includes(",");

      if (!hasComma) {
        numericValue += ",00";
      }

      if (numericValue.length > 15) {
        numericValue = numericValue.slice(0, 15);
      }

      // Adiciona o prefixo "R$ "
      if (!precoFormatado.startsWith("R$ "))
        precoFormatado = "R$ " + precoFormatado;

      this.novaViagem.price_confort = precoFormatado;

      precoFormatado = this.novaViagem.price_econ.replace(/\./g, ",");

      // Limita o tamanho do campo para 15 caracteres (incluindo "R$ ")
      if (precoFormatado.length > 14) {
        precoFormatado = precoFormatado.slice(0, 14);
      }

      // Adiciona o prefixo "R$ "
      if (!precoFormatado.startsWith("R$ ")) {
        precoFormatado = "";
        precoFormatado = "R$ " + precoFormatado;
      }
      if (precoFormatado.includes(",")) {
        if (precoFormatado.length > precoFormatado.search(",") + 3) {
          precoFormatado = precoFormatado.slice(
            0,
            precoFormatado.search(",") + 3
          );
        }
      }
      this.novaViagem.price_econ = precoFormatado;
    },
  },
};
</script>

<style scoped>
/* Estilos específicos do componente */
</style>
