import requests
import os
from dotenv import dotenv_values

# Carrega variáveis do .env (se existir), senão usa o padrão
config = dotenv_values(".env")
BASE_URL = config.get("BASE_URL", "http://localhost:8000")


def exibir_filmes(filmes: list):
    """Exibe uma lista de filmes formatada no terminal."""
    if not filmes:
        print("\n  Nenhum filme encontrado.")
        return
    print(f"\n  {'TÍTULO':<40} {'GÊNERO':<20} {'NOTA'}")
    print("  " + "-" * 65)
    for filme in filmes:
        print(f"  {filme['titulo']:<40} {filme['genero']:<20} {filme['nota']}")


def verificar_conexao():
    """Testa se o servidor está no ar."""
    try:
        resposta = requests.get(f"{BASE_URL}/", timeout=5)
        dados = resposta.json()
        print(f"\n  ✔  {dados['mensagem']}")
        return True
    except requests.exceptions.ConnectionError:
        print("\n  ✘  Não foi possível conectar ao servidor.")
        print(f"     Certifique-se de que o servidor está rodando em {BASE_URL}")
        return False


def listar_todos():
    """Busca e exibe todos os filmes do catálogo."""
    resposta = requests.get(f"{BASE_URL}/filmes", timeout=5)
    filmes = resposta.json()
    print(f"\n  Catálogo completo — {len(filmes)} filmes encontrados:")
    exibir_filmes(filmes)


def buscar_por_nome():
    """Pede um nome ao usuário e busca filmes correspondentes."""
    nome = input("\n  Digite o nome (ou parte do nome) do filme: ").strip()
    if not nome:
        print("  Nome inválido.")
        return
    resposta = requests.get(f"{BASE_URL}/buscar/{nome}", timeout=5)
    filmes = resposta.json()
    print(f"\n  Resultado para '{nome}':")
    exibir_filmes(filmes)


def buscar_por_genero():
    """Pede um gênero ao usuário e busca filmes desse gênero."""
    generos = [
        "Ação", "Animação", "Comédia", "Crime",
        "Drama", "Fantasia", "Ficção Científica", "Romance", "Terror"
    ]
    print("\n  Gêneros disponíveis:")
    for i, g in enumerate(generos, start=1):
        print(f"    [{i}] {g}")

    escolha = input("\n  Escolha o número do gênero (ou digite manualmente): ").strip()

    if escolha.isdigit() and 1 <= int(escolha) <= len(generos):
        genero = generos[int(escolha) - 1]
    else:
        genero = escolha

    resposta = requests.get(f"{BASE_URL}/genero/{genero}", timeout=5)
    filmes = resposta.json()
    print(f"\n  Filmes do gênero '{genero}':")
    exibir_filmes(filmes)


def menu():
    """Exibe o menu principal e retorna a opção escolhida."""
    print("\n" + "=" * 50)
    print("       🎬  CATÁLOGO DE FILMES — CLIENTE")
    print("=" * 50)
    print("  [1] Listar todos os filmes")
    print("  [2] Buscar filme por nome")
    print("  [3] Buscar filmes por gênero")
    print("  [0] Sair")
    print("=" * 50)
    return input("  Escolha uma opção: ").strip()


def main():
    print("\n  Verificando conexão com o servidor...")
    if not verificar_conexao():
        return

    while True:
        opcao = menu()

        if opcao == "1":
            listar_todos()
        elif opcao == "2":
            buscar_por_nome()
        elif opcao == "3":
            buscar_por_genero()
        elif opcao == "0":
            print("\n  Encerrando cliente. Até mais!\n")
            break
        else:
            print("\n  Opção inválida. Tente novamente.")

        input("\n  Pressione Enter para continuar...")


if __name__ == "__main__":
    main()