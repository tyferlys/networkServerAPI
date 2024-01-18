from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    PrimaryKeyConstraint, ForeignKey
)
from src.database.database import Base


class NetworkReview(Base):
    __tablename__ = "NetworksReviews"
    id_network = Column(Integer, ForeignKey("Networks.id"), primary_key=True)
    id_user = Column(Integer, ForeignKey("Users.id"), primary_key=True)
    text = Column(String, nullable=False)

