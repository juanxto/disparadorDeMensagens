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