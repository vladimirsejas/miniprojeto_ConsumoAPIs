import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "http://localhost:8000")


def verificar_status():
    """Faz uma requisicao GET para verificar se o servidor esta online."""
    print("\nVerificando status do servidor...")
    response = requests.get(f"{BASE_URL}/status")
    data = response.json()
    print(f"Status: {data['status']}")
    print(f"Versao: {data['versao']}")
    print(f"Mensagem: {data['mensagem']}")


def consultar_clima(cidade: str):
    """Faz uma requisicao POST com o nome da cidade e exibe o clima."""
    print(f"\nConsultando clima de: {cidade}")
    payload = {"cidade": cidade}
    response = requests.post(f"{BASE_URL}/clima", json=payload)

    if response.status_code == 200:
        data = response.json()
        print(f"Cidade:           {data['cidade']} - {data['pais']}")
        print(f"Temperatura:      {data['temperatura']}")
        print(f"Sensacao termica: {data['sensacao_termica']}")
        print(f"Umidade:          {data['umidade']}")
        print(f"Vento:            {data['vento']}")
        print(f"Condicao:         {data['descricao'].capitalize()}")
    else:
        error = response.json()
        print(f"Erro {response.status_code}: {error['detail']}")


def main():
    print("=" * 45)
    print("   CLIENTE DA API - MINI PROJETO FATEC")
    print("=" * 45)

    verificar_status()

    cidades = ["Rio Claro", "Sao Paulo", "Tokyo", "CidadeInexistente123"]
    for cidade in cidades:
        consultar_clima(cidade)

    print("\n" + "=" * 45)
    print("   Consultas finalizadas!")
    print("=" * 45)


if __name__ == "__main__":
    main()