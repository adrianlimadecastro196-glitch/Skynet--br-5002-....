import json
import os

ARQUIVO = "memoria.json"

def carregar_memoria():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r") as f:
            return json.load(f)
    return []

def salvar_memoria(historico):
    with open(ARQUIVO, "w") as f:
        json.dump(historico[-100:], f, ensure_ascii=False, indent=2)
