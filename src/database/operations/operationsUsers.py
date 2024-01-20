from sqlalchemy.orm import joinedload

from src.database.database import SessionLocal
from src.database.models.Network import Network, NetworkReview, User
from src.database.models.NetworkLike import NetworkLike


def getAllUsers():
    session = SessionLocal()

    try:
        users = (session.query(User).options(
            joinedload(User.likes),
            joinedload(User.reviews).joinedload(NetworkReview.network)
        ).all())
        return users
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()
