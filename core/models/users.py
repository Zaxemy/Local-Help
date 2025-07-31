from sqlalchemy import String
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from .posts import PostModel


class UserModel(Base):
    __tablename__ = "Users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(18), unique=True)
    posts: Mapped[list["PostModel"]] = relationship(back_populates="user")
