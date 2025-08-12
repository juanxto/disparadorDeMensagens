# 📨 Disparador de Mensagens

Sistema automatizado para envio de mensagens no WhatsApp usando Python, Supabase e Z-API.

## ⚙️ Setup do Projeto

### 1. Clone o repositório
```bash
git clone https://github.com/juanxto/disparadorDeMensagens.git
cd disparadorDeMensagens
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure o Supabase

Crie uma tabela chamada `contatos` com a seguinte estrutura:

```sql
CREATE TABLE contatos (
  id UUID PRIMARY KEY,
  nome TEXT NOT NULL,
  telefone TEXT NOT NULL
);
```

Insira alguns contatos de teste:
```sql
INSERT INTO contatos (nome, telefone) VALUES 
('Maria Silva', '11920437941'),
('João Santos', '11980851373'),
('Ana Costa', '11975389068');
```

### 4. Configure a Z-API

1. Acesse [Z-API](https://z-api.io) e crie uma conta gratuita
2. Conecte seu WhatsApp
3. Copie: `Instance ID`, `Token` e `Client Token`

### 5. Configure as variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com base no modelo `.env.example`:

```env
SUPABASE_URL=sua_url_do_supabase
SUPABASE_KEY=sua_chave_do_supabase
ZAPI_INSTANCE_ID=seu_instance_id
ZAPI_TOKEN=seu_token
ZAPI_CLIENT_TOKEN=seu_client_token
```

## 🚀 Como executar

```bash
python main.py
```

## 🔒 Segurança

- ✅ Credenciais em variáveis de ambiente
- ✅ `.env` adicionado ao `.gitignore`
- ✅ Validação de todas as variáveis obrigatórias
- ✅ Tratamento de erros em todas as operações

## 🐛 Troubleshooting

**Erro: "Verifique se todas as variáveis estão definidas"**
- Verifique se o arquivo `.env` existe e está preenchido

**Erro: "Nenhum contato encontrado"**
- Confirme se a tabela `contatos` existe no Supabase
- Verifique se há registros na tabela

**Erro de envio Z-API**
- Confirme se o WhatsApp está conectado na Z-API
- Verifique se os tokens estão corretos

## 👨‍💻 Autor

Desenvolvido por **Juan Pablo Rebelo Coelho**