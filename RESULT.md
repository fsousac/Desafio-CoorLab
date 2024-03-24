# Resultado - Desáfio CoorLab

## Descrição do Projeto

O projeto consiste em uma aplicação web para gerenciamento de viagens, com funcionalidades de adicionar novas viagens e listar as viagens existentes.

## Dificuldades de Criação

Durante o desenvolvimento do projeto, algumas dificuldades foram encontradas:

### Front-end

- **Validação de Entrada**: Implementar a validação de entrada, especialmente para formatar corretamente os preços e outros campos, foi desafiador devido à complexidade das regras de formatação.

- **Integração com Vue Router**: Integrar o Vue Router para criar a navegação entre os componentes AddTrip e ListTrip exigiu um tempo adicional para configurar corretamente.

### Back-end

- **Persistência de Dados**: A implementação da persistência de dados usando um arquivo JSON como banco de dados apresentou desafios para garantir a integridade dos dados e evitar a sobrescrição desnecessária de dados existentes.

- **Gerenciamento de Requisições**: Lidar com as solicitações HTTP no back-end, especialmente ao processar dados enviados pelo cliente, exigiu um cuidadoso gerenciamento para garantir a segurança e a integridade dos dados.

## Executando o Projeto

Para executar o projeto, siga as instruções abaixo:

1. Certifique-se de ter o Python e o Django instalados em sua máquina.

2. Clone o repositório do projeto:

   ```bash
   git clone https://github.com/fsousac/Desafio-CoorLab.git
   ```

3. Navegue até o diretório do projeto:

   ```bash
   cd app/
   ```

4. Execute o script `run.sh`:
   ```bash
   chmod +x run.sh
   ./run.sh
   ```

Isso iniciará o servidor Django na porta 3000 e o servidor de desenvolvimento Vue.js na porta 8080, permitindo que você acesse a aplicação no seu navegador.

Acesse a aplicação em: `http://localhost:8080`

## Conclusão

Apesar dos desafios encontrados durante o desenvolvimento, o projeto foi concluído com relativo sucesso, fornecendo uma base sólida para futuras iterações e melhorias. Apesar de não ter sido possível realizar uma melhor filtragem dos dados no front-end e não terem sido implementados todos os endpoints REST da api, foi uma experiência muito enriquecedora de aprimoramento pessoal e acredito que o core do desafio foi cumprido.
