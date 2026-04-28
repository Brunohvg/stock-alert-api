# Stock Alert API

## 📌 Descrição
API para registrar interesse de clientes em produtos sem estoque e notificá-los quando o produto estiver disponível novamente.

## 🧠 Stack
- FastAPI
- PostgreSQL (futuro)
- SQLAlchemy (futuro)

## 🚀 Como rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/Brunohvg/Stock-Alert-API.git
   ```

2. Acesse o projeto:
   ```bash
   cd stock-alert-api
   ```

3. Crie o ambiente virtual:
   ```bash
   uv venv
   ```

4. Ative o ambiente:
   - **Linux/Mac**:
     ```bash
     source .venv/bin/activate
     ```
   - **Windows**:
     ```bash
     .venv\Scripts\activate
     ```

5. Instale as dependências:
   ```bash
   uv sync
   ```

6. Execute a aplicação:
   ```bash
   fastapi dev app/main.py
   ```

7. Acesse:
   - [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 🔍 Endpoint

### Health Check
- **GET /health**: Retorna o status da aplicação.
  ```json
  {
      "status": "ok"
  }
  ```
