from sqlalchemy import (
    LargeBinary,
    Column,
    String,
    Integer,
    Boolean,
    UniqueConstraint,
    PrimaryKeyConstraint, ForeignKey
)
from sqlalchemy.orm import relationship

from src.database.database import Base
from src.database.models.NetworkLike import NetworkLike
from src.database.models.TagToNetwork import TagToNetwork


class Network(Base):
    __tablename__ = "Networks"
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
    descriptionResult = Column(String, nullable=False)
    image = Column(String, nullable=True)

    tags = relationship("Tag", secondary="TagsToNetworks", back_populates="networks")
    likes = relationship("User", secondary="NetworksLikes", back_populates="likes")
    reviews = relationship("NetworkReview", back_populates="network")

    UniqueConstraint("title", name="uq_network_title")
    PrimaryKeyConstraint("id", name="pk_network_id")


class Tag(Base):
    __tablename__ = "Tags"
    id = Column(Integer, nullable=False, primary_key=True)
    title = Column(String, nullable=False, unique=True)

    networks = relationship("Network", secondary="TagsToNetworks", back_populates="tags")

    UniqueConstraint("title", name="uq_tag_title")
    PrimaryKeyConstraint("id", name="pk_tag_id")


class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, nullable=False, primary_key=True)
    ip_address = Column(String, nullable=False, unique=True)
    username = Column(String, nullable=False)

    likes = relationship("Network", secondary="NetworksLikes", back_populates="likes")
    reviews = relationship("NetworkReview", back_populates="user")

    UniqueConstraint("ip_address", name="uq_user_ip_address")
    PrimaryKeyConstraint("id", name="pk_user_id")


class NetworkReview(Base):
    __tablename__ = "NetworksReviews"
    id_network = Column(Integer, ForeignKey("Networks.id"), primary_key=True)
    id_user = Column(Integer, ForeignKey("Users.id"), primary_key=True)
    text = Column(String, nullable=False)

    user = relationship("User", back_populates="reviews")
    network = relationship("Network", back_populates="reviews")


