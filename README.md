<div align="center">
  Suzano - Python Developer
  <a href="https://web.dio.me/track/823e5de7-79a5-44fe-a472-cfe6bb0fec00">
    <img src="https://assets.dio.me/wqFNFD1_7AKN1MpbZvurY1cUcpUXQ2ELMfW5Bi9R8VM/f:webp/h:120/q:80/L3RyYWNrcy9lN2MzZjVkNy0yMTEwLTQ3N2YtYmYxMS0wNjg3MjQzMjZjYzEucG5n" width="300" alt="imagem Python Developer" />
  </a>
</div>

# 🏦 Sistema Bancário em Python 💻

Um sistema bancário simples desenvolvido em Python para o desafio do Bootcamp Suzano - Python Developer para gerenciar operações básicas de depósito, saque e extrato. Este projeto foi criado como parte de um desafio de programação.

---

## 🛠️ Tecnologias Usadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)
![Terminal](https://img.shields.io/badge/Terminal-4D4D4D?style=for-the-badge&logo=windows-terminal&logoColor=white)

---

## 📋 Índice

- [Funcionalidades](#-funcionalidades)
- [Como Usar](#-como-usar)
- [Requisitos](#-requisitos)
- [Instalação](#-instalação)
- [Estrutura do Projeto](#-estrutura-do-projeto)
- [Contribuição](#-contribuição)
- [Licença](#-licença)
- [Contato](#-contato)

---

## 🚀 Funcionalidades

O sistema bancário oferece as seguintes funcionalidades:

1. **Depósito** 💰
   - Permite ao usuário depositar valores positivos na conta.
   - Todos os depósitos são registrados no extrato.

2. **Saque** 💳
   - Permite ao usuário sacar valores da conta, com as seguintes regras:
     - Limite de **3 saques diários**.
     - Limite máximo de **R$ 500,00 por saque**.
     - Verificação de saldo disponível.
   - Todos os saques são registrados no extrato.

3. **Extrato** 📜
   - Exibe todas as movimentações (depósitos e saques).
   - Mostra o saldo atual da conta.
   - Se não houver movimentações, exibe uma mensagem informativa.

4. **Sair** 🚪
   - Encerra o sistema.

---

## 🛠️ Como Usar

### Passo a Passo

1. **Execute o Sistema**:
   - Abra o terminal e navegue até o diretório do projeto.
   - Execute o seguinte comando:
     ```bash
     python sistema_bancario.py
     ```

2. **Menu de Opções**:
   - O sistema exibirá um menu com as seguintes opções:
     ```
     --- Sistema Bancário ---
     1. Depositar
     2. Sacar
     3. Extrato
     4. Sair
     ```

3. **Depositar**:
   - Escolha a opção `1` e insira o valor a ser depositado.
   - O valor será adicionado ao saldo e registrado no extrato.

4. **Sacar**:
   - Escolha a opção `2` e insira o valor a ser sacado.
   - O sistema verificará se o valor é válido e se há saldo suficiente.
   - O valor será subtraído do saldo e registrado no extrato.

5. **Extrato**:
   - Escolha a opção `3` para visualizar todas as movimentações e o saldo atual.

6. **Sair**:
   - Escolha a opção `4` para encerrar o sistema.

---

## 📋 Requisitos

- **Python 3.6 ou superior** 🐍
- **Terminal ou Prompt de Comando** 💻

---

## 🔧 Instalação

1. **Clone o Repositório**:
   ```bash
   git clone https://github.com/mauricioliveir/desafio_banco.git

2. **Navegue até o Diretório**:

   ```bash
   cd desafio_banco

3. **Execute o Sistema**:

   ```bash
   python desafio_bancoario.py


## 📂 Estrutura do Projeto
sistema-bancario-python/
├── sistema_bancario.py  # Código principal do sistema
├── README.md            # Documentação do projeto
└── .gitignore           # Arquivo para ignorar arquivos desnecessários no Git

## 🤝 Contribuição
Contribuições são bem-vindas! Siga os passos abaixo:

1. **Faça um fork do projeto**.

2. **Crie uma nova branch com sua feature**:

   ```bash
   git checkout -b minha-feature

3. **Commit suas mudanças**:

   ```bash
   git commit -m "Adicionei uma nova funcionalidade"

4. **Push para a branch**:

   ```bash
   git push origin minha-feature

5. **Abra um Pull Request**.

## 📜 Licença
Este projeto está licenciado sob a licença MIT. Consulte o arquivo LICENSE para mais detalhes.

## 📞 Contato

Se você tiver alguma dúvida ou sugestão, sinta-se à vontade para entrar em contato:

- **Nome**: Mauricio
- **Email**: [manutencaomauricio81@gmail.com](mailto:manutencaomauricio81@gmail.com)
- **GitHub**: [@mauricioliveir](https://github.com/mauricioliveir)

## 🎉 Agradecimentos
À equipe DIO e do Bootcamp Suzano - Python Developer

À comunidade Python por fornecer ferramentas incríveis para desenvolvimento.

---

<div align="center">
  Feito com ❤️ por **Mauricio** 🚀  
  <a href="https://github.com/mauricioliveir">
    <img src="https://avatars.githubusercontent.com/u/83318403?v=4" width="100" alt="Avatar de Mauricio" />
  </a>
</div>