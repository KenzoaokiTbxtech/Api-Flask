# API Flask

API REST desenvolvida com Flask e SQLAlchemy para gerenciamento de dados. 

## 📋 Descrição

Esta é uma API RESTful construída com Flask que utiliza SQLAlchemy para persistência de dados. A aplicação está containerizada com Docker, facilitando o deploy e desenvolvimento.

## 🚀 Tecnologias

- **Flask 3.0.0** - Framework web
- **Flask-SQLAlchemy 3.1.1** - ORM para banco de dados
- **Python 3.x** - Linguagem de programação
- **Docker** - Containerização
- **SQLite** - Banco de dados (desenvolvimento)

## 📦 Estrutura do Projeto

```
Api-Flask/
├── src/
│   ├── main.py          # Arquivo principal da aplicação
│   ├── models.py        # Modelos de dados
│   ├── db.py           # Configuração do banco de dados
│   ���── test.py         # Testes unitários
│   ├── requirements.txt # Dependências Python
│   └── instance/       # Dados do banco (SQLite)
├── Dockerfile          # Configuração do container
└── docker-compose.yml  # Orquestração do container
```

## 🐳 Como Rodar com Docker

### Pré-requisitos

- Docker instalado
- Docker Compose instalado

### Passos para Executar

1. **Clone o repositório**
   ```bash
   git clone https://github.com/KenzoaokiTbxtech/Api-Flask.git
   cd Api-Flask
   ```

2. **Build e execute o container**
   ```bash
   docker-compose up --build
   ```

3. **Acesse a API**
   
   A aplicação estará disponível em:  `http://localhost:5000`

### Comandos Úteis

- **Parar o container:**
  ```bash
  docker-compose down
  ```

- **Executar em background:**
  ```bash
  docker-compose up -d
  ```

- **Ver logs:**
  ```bash
  docker-compose logs -f
  ```

- **Reconstruir o container:**
  ```bash
  docker-compose up --build --force-recreate
  ```

## 🔧 Variáveis de Ambiente

A aplicação utiliza as seguintes variáveis de ambiente configuradas no `docker-compose.yml`:

- `FLASK_ENV=development` - Define o ambiente de desenvolvimento

## 🧪 Executar Testes

Para executar os testes dentro do container:

```bash
docker-compose exec api pytest src/test.py -v
```

## 📝 Desenvolvimento Local

Se preferir rodar sem Docker: 

1. **Crie um ambiente virtual**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # ou
   venv\Scripts\activate     # Windows
   ```

2. **Instale as dependências**
   ```bash
   pip install -r src/requirements.txt
   ```

3. **Execute a aplicação**
   ```bash
   python src/main.py
   ```
