# 🐍 Atividades Python — Eduardo Hernandes

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

Este repositório contém três atividades introdutórias de Python, desenvolvidas para praticar conceitos fundamentais da linguagem como estruturas condicionais, operadores lógicos, manipulação de listas e dicionários.

---

## 📚 Índice

- [Atividade 1 — Validador de Senha e Acesso](#-atividade-1--validador-de-senha-e-acesso)
- [Atividade 2 — Classificador de Prioridade de Chamados](#-atividade-2--classificador-de-prioridade-de-chamados)
- [Atividade 3 — Acessando e Validando Listas](#-atividade-3--acessando-e-validando-listas)
- [Como Executar](#-como-executar)

---

## 🔐 **Atividade 1 — Validador de Senha e Acesso**

**Conceitos praticados:** `if`, `else`, `elif`, operadores lógicos (`and`, `or`)

### 🎯 Objetivo

Desenvolver um sistema simples de validação de login que verifica credenciais e aplica regras de segurança.

### 📋 Requisitos

#### 1. Variáveis pré-definidas
```python
login_salvo = "admin_ti"
senha_salva = "Sistema@123"
```

#### 2. Entrada do usuário
- Solicitar `login_digitado`
- Solicitar `senha_digitada`

#### 3. Regras de validação

| Condição | Resultado |
|----------|-----------|
| `login_digitado == login_salvo` **E** `senha_digitada == senha_salva` | ✅ **Acesso Concedido.** Bem-vindo ao Painel de Controle. |
| `login_digitado == "guest"` **OU** `senha_digitada == "123456"` | ⚠️ **Acesso Negado:** Credenciais de baixo risco ou padrão de segurança. |
| Nenhuma condição atendida | ❌ **Erro de Acesso:** Login ou Senha inválidos. |

### 💡 Exemplo de execução

```
Digite o login: admin_ti
Digite a senha: Sistema@123
✅ Acesso Concedido. Bem-vindo ao Painel de Controle.
```

---

## 🎫 **Atividade 2 — Classificador de Prioridade de Chamados**

**Conceitos praticados:** `elif`, condições aninhadas, dicionários

### 🎯 Objetivo

Criar um sistema automático de classificação de prioridade para chamados de manutenção de TI.

### 📋 Requisitos

#### 1. Estrutura inicial do chamado
```python
chamado = {
    "equipamento": "Servidor Principal",
    "tempo_parado_horas": 5,
    "setor": "Financeiro",
    "status": "aberto"
}
```

#### 2. Lógica de classificação

| Prioridade | Condições |
|------------|-----------|
| **P1 — Crítica** 🔴 | `equipamento == "Servidor Principal"` **OU** `tempo_parado_horas > 4` |
| **P2 — Alta** 🟡 | `setor == "Financeiro"` **E** `tempo_parado_horas > 1` |
| **P3 — Normal** 🟢 | Todos os outros casos |

#### 3. Saída esperada
Exibir o nome do equipamento e sua prioridade definida (P1, P2 ou P3).

### 💡 Exemplo de execução

```
Equipamento: Servidor Principal
Prioridade: P1 — Crítica 🔴
```

---

## 📦 **Atividade 3 — Acessando e Validando Listas**

**Conceitos praticados:** `if`, operador `in`, manipulação de listas (`.append()`)

### 🎯 Objetivo

Desenvolver um script que previne a duplicação de softwares críticos antes da instalação.

### 📋 Requisitos

#### 1. Lista inicial
```python
softwares_criticos = ["ERP", "Banco de Dados SQL", "Firewall"]
```

#### 2. Entrada do usuário
Solicitar o nome do `software_novo` a ser instalado.

#### 3. Verificação

| Condição | Ação |
|----------|------|
| `software_novo in softwares_criticos` | ⚠️ Exibir: "Atenção: Este software é crítico e já está instalado. Nenhuma alteração é necessária." |
| `software_novo` não existe na lista | ✅ Informar início da instalação<br>📝 Adicionar à lista com `.append()`<br>📋 Exibir lista atualizada |

### 💡 Exemplo de execução

```
Digite o nome do software: Antivírus
✅ Iniciando instalação de 'Antivírus'...
📋 Softwares críticos atualizados: ['ERP', 'Banco de Dados SQL', 'Firewall', 'Antivírus']
```

---

## 🚀 Como Executar

### Pré-requisitos
- Python 3.8 ou superior instalado

### Passos

1. **Clone o repositório**
```bash
git clone https://github.com/seu-usuario/atividades-python.git
cd atividades-python
```

2. **Execute cada atividade**
```bash
# Atividade 1
python atividade1_validador_acesso.py

# Atividade 2
python atividade2_classificador_chamados.py

# Atividade 3
python atividade3_validacao_listas.py
```

---

## 🛠️ Tecnologias Utilizadas

- **Python 3.8+** — Linguagem de programação
- **Estruturas condicionais** — if, elif, else
- **Operadores lógicos** — and, or, not
- **Estruturas de dados
