# Mini Projeto API - Consumo de APIs
Projeto desenvolvido para a disciplina de Inteligencia Artificial
Fatec Rio Claro - 2 Semestre - 2025
## Descricao

Este projeto implementa um servidor de API com FastAPI e um cliente
Python que consome essa API. O servidor consulta a API publica do
OpenWeatherMap e retorna informacoes climaticas de qualquer cidade.

## Estrutura do Projeto

mini_projeto_api/
├── README.md  
├── requirements.txt
├── .gitignore
├── server/
│   ├── app/
│   │   ├── __init__.py
│   │   └── main.py
│   └── .env.example
└── client/
    ├── main.py
    └── .env.example

## Como rodar
### 1. Instalar dependencias
pip install -r requirements.txt
### 2. Configurar variaveis de ambiente
No servidor, copie o arquivo .env.example e renomeie para .env
Adicione sua chave da API do OpenWeatherMap
No cliente, copie o arquivo .env.example e renomeie para .env

### 3. Rodar o servidor
cd server/app
python main.py

### 4. Rodar o cliente
cd client
python main.py

## Endpoints
GET /status
Retorna o status do servidor.
Resposta: {"status": "ok", "versao": "1.0", "mensagem": "Servidor online!"}

POST /clima
Recebe o nome de uma cidade e retorna dados climaticos.
Corpo: {"cidade": "Rio Claro"}
Resposta: temperatura, umidade, vento, descricao

## Integrantes

- Mateo (mateozin) - Servidor backend
- Vladimir (vladimirsejas) - Cliente, README, configuracao

## Dependencias

fastapi, uvicorn, requests, httpx, python-dotenv, pydantic