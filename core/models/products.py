from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class ProductModel(Base):
    __tablename__ = "Products"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    price: Mapped[int]
    description: Mapped[str]