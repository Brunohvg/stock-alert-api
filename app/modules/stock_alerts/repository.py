from sqlalchemy import select
from sqlalchemy.orm import Session

from .models import StockAlert


class StockAlertRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_stock_alert(self, stock_alert: StockAlert) -> StockAlert:
        self.db.add(stock_alert)
        self.db.commit()
        self.db.refresh(stock_alert)

        return stock_alert

    def get_all_alerts(self) -> list[StockAlert]:
        stmt = select(StockAlert).order_by(StockAlert.created_at.desc()).limit(100)
        result = self.db.execute(stmt).scalars().all()

        return result

    def get_by_phone_and_product_and_variation_id(
        self,
        phone: str,
        external_product_id: str,
        variation_id: str | None,
    ) -> StockAlert | None:
        stmt = select(StockAlert).where(
            StockAlert.customer_phone == phone,
            StockAlert.external_product_id == external_product_id,
            StockAlert.variation_id == variation_id,
        )

        result = self.db.execute(stmt).scalars().first()

        return result

    def get_by_id(self, alert_id: int) -> StockAlert | None:
        stmt = select(StockAlert).where(StockAlert.id == alert_id)
        result = self.db.execute(stmt).scalars().first()
        return result
