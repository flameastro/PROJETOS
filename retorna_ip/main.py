# Capturando o MEU IP
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/125.0.6422.113 Safari/537.36 "
        "Edg/125.0.2535.67"
    ),
    "Accept": (
        "text/html,application/xhtml+xml,application/xml;"
        "q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,"
        "application/signed-exchange;v=b3;q=0.7"
    ),
    "Accept-Language": "en-US,en;q=0.9,pt-BR;q=0.8,pt;q=0.7",
    "Connection": "keep-alive",
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "none",
    "Sec-Fetch-User": "?1",
    "Sec-Ch-Ua": (
        '"Chromium";v="125", "Microsoft Edge";v="125", '
        '"Not.A/Brand";v="24"'
    ),
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": '"Windows"',
    "DNT": "1",
    "TE": "trailers"
}


def encontrar_meu_ip():
    print("Tentando capturar o seu IP...")

    try:
        r = requests.get("https://meuip.com.br/", headers=headers)
        soup = BeautifulSoup(r.content, "html.parser")

        IP = soup.find("h3").getText().strip()

        return IP
    except requests.ConnectionError as conn_e:
        return f"Erro de conexão, verifique a sua internet. {conn_e}"
    except requests.exceptions.Timeout as timeout_e:
        return f"Não foi possível encontrar seu IP. Tempo limite excedido. {timeout_e}"
    except Exception as e:
        return f"Erro: {e}."


print(encontrar_meu_ip())
