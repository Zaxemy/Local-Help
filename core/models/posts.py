from typing import TYPE_CHECKING
from sqlalchemy import ForeignKey, String, Text
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship



if TYPE_CHECKING:
    from .users import UserModel


class PostModel(Base):
    __tablename__ = "Posts"

    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=False)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))
    user: Mapped["UserModel"] = relationship(back_populates="posts")
