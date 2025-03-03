# 🏦 Sistema Bancário em Python 💻

Um sistema bancário simples desenvolvido em Python para gerenciar operações básicas de depósito, saque e extrato. Este projeto foi criado como parte de um desafio de programação para modernizar as operações de um banco.

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

2. **Navegue até o Diretório:**:
    ```bash
    cd desafio_banco

3. **Execute o script:**:
    ```bash
    python desafio_banco.py

## 📂 Estrutura do Projeto

    ```bash
    sistema-bancario-python/
    ├── desafio_banco.py
    ├── README.md
    └── .gitignore

