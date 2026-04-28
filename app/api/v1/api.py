from fastapi import APIRouter

from app.modules.stock_alerts.router import router as stock_alerts_router

v1_router = APIRouter()


# Rota de saúde específica da v1 (opcional)
@v1_router.get('/health', tags=['Health'])
async def health_check():
    return {'status': 'ok', 'version': 'v1'}


# Inclui o módulo de alertas que você já criou
v1_router.include_router(stock_alerts_router, prefix='/stock-alerts', tags=['Stock Alerts'])
