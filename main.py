import os
from supabase import create_client, Client
import requests
from dotenv import load_dotenv

# Carregar variáveis do .env
load_dotenv()

# Ler variáveis do .env
SUPABASE_URL = os.getenv("SUPABASE_URL")
SUPABASE_KEY = os.getenv("SUPABASE_KEY")
ZAPI_INSTANCE_ID = os.getenv("ZAPI_INSTANCE_ID")
ZAPI_TOKEN = os.getenv("ZAPI_TOKEN")
ZAPI_CLIENT_TOKEN = os.getenv("ZAPI_CLIENT_TOKEN")

# Verificar se todas as variáveis foram carregadas
if not all([SUPABASE_URL, SUPABASE_KEY, ZAPI_INSTANCE_ID, ZAPI_TOKEN, ZAPI_CLIENT_TOKEN]):
    raise ValueError("❌ Erro: Verifique se todas as variáveis estão definidas no arquivo .env")

# Criar cliente Supabase
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def buscar_contatos():
    """Busca contatos no Supabase"""
    try:
        response = supabase.table("contatos").select("*").execute()
        contatos = response.data
        if not contatos:
            print("⚠️ Nenhum contato encontrado.")
        return contatos
    except Exception as e:
        print(f"❌ Erro ao buscar contatos: {e}")
        return []


def enviar_mensagem(numero, nome):
    """Envia mensagem para o número informado usando a Z-API"""
    # Garantir que o número esteja no formato correto
    numero = "".join(filter(str.isdigit, str(numero)))  # remove caracteres não numéricos
    if not numero.startswith("55"):
        numero = f"55{numero}"

    # URL correta com token
    url = f"https://api.z-api.io/instances/{ZAPI_INSTANCE_ID}/token/{ZAPI_TOKEN}/send-text"

    headers = {
        "Client-Token": ZAPI_CLIENT_TOKEN,  # Usar o Client-Token correto
        "Content-Type": "application/json"
    }

    payload = {
        "phone": numero,
        "message": f"Olá {nome}, tudo bem com você?"
    }

    try:
        r = requests.post(url, json=payload, headers=headers)

        try:
            resposta_json = r.json()
        except Exception:
            resposta_json = {"raw": r.text}

        if r.status_code == 200:
            print(f"✅ Mensagem enviada para {nome} ({numero})")
        else:
            print(f"⚠️ Tentativa para {nome} ({numero}) — Status: {r.status_code} — Resposta: {resposta_json}")

    except Exception as e:
        print(f"❌ Erro ao enviar mensagem para {nome}: {e}")