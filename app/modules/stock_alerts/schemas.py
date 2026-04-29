from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel, EmailStr, Field


class StockAlertCreate(BaseModel):
    customer_name: str = Field(..., description='Nome do cliente')

    customer_phone: str = Field(..., description='Telefone do cliente')

    customer_email: EmailStr | None = Field(None, description='Email do cliente')

    accepts_marketing: bool = Field(False, description='Aceita receber marketing')

    product_name: str = Field(..., description='Nome do produto')

    requested_quantity: int = Field(1, ge=1, description='Quantidade desejada')

    external_product_id: str = Field(..., description='ID externo do produto')
    price_product: Decimal | None = Field(
    None,
    max_digits=10,
    decimal_places=2,
    description='Preço do produto no momento do cadastro do alerta'
        )
    variation_id: str | None = Field(None, description='ID da variação do produto')
    variation_name: str | None = Field(None, description='Nome da variação do produto')


class StockAlertResponse(BaseModel):
    id: int
    customer_name: str
    customer_phone: str
    customer_email: EmailStr | None
    accepts_marketing: bool
    product_name: str
    requested_quantity: int
    external_product_id: str
    price_product: Decimal | None
    variation_id: str | None
    variation_name: str | None
    is_notified: bool
    created_at: datetime
    updated_at: datetime
    notified_at: datetime | None

    model_config = {'from_attributes': True}
