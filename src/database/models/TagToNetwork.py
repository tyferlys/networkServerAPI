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


class TagToNetwork(Base):
    __tablename__ = "TagsToNetworks"
    id_network = Column(Integer, ForeignKey("Networks.id"), primary_key=True)
    id_tags = Column(Integer, ForeignKey("Tags.id"), primary_key=True)

