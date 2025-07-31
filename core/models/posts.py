from sqlalchemy import ForeignKey, String, Text
from .base import Base
from sqlalchemy.orm import Mapped, mapped_column


class PostModel(Base):
    __tablename__ = "Posts"

    
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str] = mapped_column(String(200), unique=False)
    body: Mapped[str] = mapped_column(Text, default="", server_default="")
    user_id: Mapped[int] = mapped_column(ForeignKey("Users.id"))

