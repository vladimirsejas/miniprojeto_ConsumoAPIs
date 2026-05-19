from fastapi import FastAPI
from difflib import get_close_matches
import json

app = FastAPI()

with open("server/app/catalogo.json", "r", encoding="utf-8") as arquivo: #catalogo com alguns filmes aleatorios
    catalogo = json.load(arquivo)

@app.get("/")
def home():
    return {"mensagem": "API de Filmes funcionando"} #confirmação de funcionamento


@app.get("/filmes")
def listar_filmes(): #função para listar o catalogo
    return catalogo


@app.get("/buscar/{nome}")
def buscar_por_nome(nome): #função para buscar algum filme pelo nome (não precisa ser nome exato)
    nome = nome.lower()
    resultado = []
    for filme in catalogo:
        titulo = filme["titulo"].lower()
        if nome in titulo:
            resultado.append(filme)
            continue
        similar= get_close_matches(nome,[titulo],n=1,cutoff=0.3)
        if similar:
            resultado.append(filme)
    return resultado


@app.get("/genero/{genero}")
def buscar_genero(genero): #função para buscar algum filme utilizando o genero dele

    resultado = []

    for filme in catalogo:
        if filme["genero"].lower() == genero.lower():
            resultado.append(filme)

    return resultado