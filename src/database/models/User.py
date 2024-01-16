from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    PrimaryKeyConstraint
)
from src.database.database import Base


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, nullable=False, primary_key=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    name = Column(String, nullable=True)
    surname = Column(String, nullable=True)
    age = Column(String, nullable=True)
    description = Column(String, nullable=True)

    UniqueConstraint("username", name="uq_user_username")
    PrimaryKeyConstraint("id", name="pk_user_id")