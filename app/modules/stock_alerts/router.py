from http import HTTPStatus

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.session import get_db

from .repository import StockAlertRepository
from .schemas import StockAlertCreate, StockAlertResponse
from .service import StockAlertService

router = APIRouter(tags=['Stock Alerts'])


@router.get('/', status_code=HTTPStatus.OK, response_model=list[StockAlertResponse])
async def list_stock_alerts(db: Session = Depends(get_db)):
    repo = StockAlertRepository(db)
    service = StockAlertService(repo)

    return service.list_alerts()


@router.get('/{alert_id}', status_code=HTTPStatus.OK, response_model=StockAlertResponse)
async def retrieve_stock_alert(alert_id: int, db: Session = Depends(get_db)):
    repo = StockAlertRepository(db)
    service = StockAlertService(repo)

    alert = service.get_alert_by_id(alert_id)

    if not alert:
        raise HTTPException(status_code=404, detail='Alerta não encontrado')

    return alert


@router.post('/', status_code=HTTPStatus.CREATED, response_model=StockAlertResponse)
async def create_stock_alert(data: StockAlertCreate, db: Session = Depends(get_db)):
    repo = StockAlertRepository(db)
    service = StockAlertService(repo)

    try:
        return service.create_alert(data)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
