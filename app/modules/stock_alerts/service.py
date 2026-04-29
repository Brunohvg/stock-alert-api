from .models import StockAlert
from .repository import StockAlertRepository
from .schemas import StockAlertCreate


class StockAlertService:
    """
    Camada de regra de negócio.

    Recebe o repository e usa seus métodos
    para executar operações.
    """

    def __init__(self, repository: StockAlertRepository):
        """
        Inicializa o service.

        Args:
            repository: instância do repository
        """
        self.repository = repository

    def create_alert(self, data: StockAlertCreate) -> StockAlert:
        v_id = data.variation_id if data.variation_id and str(data.variation_id).strip() else None

        existing = self.repository.get_by_phone_and_product_and_variation_id(
            data.customer_phone,
            data.external_product_id,
            v_id,
        )
        if existing:
            raise ValueError('Já existe alerta para esse produto')

        stock_alert = StockAlert(
            customer_name=data.customer_name,
            customer_phone=data.customer_phone,
            customer_email=data.customer_email,
            accepts_marketing=data.accepts_marketing,
            product_name=data.product_name,
            requested_quantity=data.requested_quantity,
            external_product_id=data.external_product_id,
            variation_id=v_id,
            variation_name=data.variation_name,
            price_product=data.price_product,
        )

        return self.repository.create_stock_alert(stock_alert)

    def list_alerts(self):
        """Lista todos os alertas cadastrados."""
        return self.repository.get_all_alerts()

    def get_alert_by_id(self, alert_id: int):
        return self.repository.get_by_id(alert_id)
