from fastapi import FastAPI
from app.api.v1.api import v1_router

tags_metadata = [
    {"name": "Stock Alerts", "description": "Gerenciamento de alertas de estoque."},
    {"name": "Health", "description": "Monitoramento do sistema."},
]

app = FastAPI(
    title="Stock Alert API",
    openapi_tags=tags_metadata  # Isso fixa a ordem no Swagger
)
# Aqui você monta a árvore principal
app.include_router(v1_router, prefix="/api/v1")

