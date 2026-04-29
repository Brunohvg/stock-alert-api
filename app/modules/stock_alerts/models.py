from datetime import datetime, timezone
from decimal import Decimal

from sqlalchemy import Boolean, DateTime, Integer, Numeric, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.database.base import Base


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


class StockAlert(Base):
    __tablename__ = 'stock_alerts'

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True,
    )

    customer_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    customer_phone: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True,
    )

    customer_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    accepts_marketing: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default='false',
    )

    product_name: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    requested_quantity: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=1,
        server_default='1',
    )

    external_product_id: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        index=True,
    )
    price_product: Mapped[Decimal | None] = mapped_column(Numeric(10, 2), nullable=True)

    variation_id: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    variation_name: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    is_notified: Mapped[bool] = mapped_column(
        Boolean,
        nullable=False,
        default=False,
        server_default='false',
        index=True,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
        server_default=func.now(),
    )

    notified_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=utc_now,
        onupdate=utc_now,
        server_default=func.now(),
    )

    def __repr__(self) -> str:
        return (
            f'<StockAlert(id={self.id}, '
            f"customer_phone='{self.customer_phone}', "
            f"external_product_id='{self.external_product_id}', "
            f'is_notified={self.is_notified})>'
        )
