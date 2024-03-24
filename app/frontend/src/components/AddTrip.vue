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
          @input="novaViagem.price_confort = formatarPreco($event.target.value)"
          @blur="
            novaViagem.price_confort = adicionaCentavos($event.target.value)
          "
        />
      </div>
      <div>
        <label for="precoEconomico">Preço (Econômico):</label>
        <input
          type="text"
          id="precoEconomico"
          v-model="novaViagem.price_econ"
          required
          @input="novaViagem.price_econ = formatarPreco($event.target.value)"
          @blur="novaViagem.price_econ = adicionaCentavos($event.target.value)"
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
        <input
          type="text"
          id="poltrona"
          v-model="novaViagem.seat"
          @input="novaViagem.seat = formatarAssento($event.target.value)"
          required
        />
      </div>
      <div>
        <label for="leito">Leito:</label>
        <input
          type="text"
          id="leito"
          v-model="novaViagem.bed"
          @input="novaViagem.bed = formatarAssento($event.target.value)"
          required
        />
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
    formatarAssento(inputValue) {
      inputValue = inputValue.toUpperCase();
      inputValue = inputValue.slice(0, 3);
      return inputValue;
    },
    formatarPreco(inputValue) {
      // Remove todas as vírgulas
      let numericValue = inputValue.replace(/[^\d,.]/g, "");
      numericValue = numericValue.replace(/\./g, ",");
      const hasComma = numericValue.includes(",");

      if (!numericValue.startsWith("R$ ")) numericValue = "R$ " + numericValue;

      if (hasComma) {
        let test = numericValue.slice(
          numericValue.search(",") + 1,
          numericValue.length
        );
        test = test.replace(",", "");
        numericValue =
          numericValue.slice(0, numericValue.search(",") + 1) + test;
        numericValue = numericValue.slice(0, numericValue.search(",") + 3);
      }

      if (numericValue.length > 15) {
        numericValue = numericValue.slice(0, 15);
      }

      inputValue = numericValue;
      return inputValue;
    },
    adicionaCentavos(inputValue) {
      const hasComma = inputValue.includes(",");

      if (!hasComma) {
        inputValue += ",00";
      } else {
        while (inputValue.search(",") + 3 > inputValue.length) {
          inputValue += "0";
        }
      }
      return inputValue;
    },
  },
};
</script>

<style scoped></style>
