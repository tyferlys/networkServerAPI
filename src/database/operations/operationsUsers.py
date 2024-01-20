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


def getUser(idUser: int):
    session = SessionLocal()

    try:
        users = (session.query(User).where(User.id == idUser).options(
            joinedload(User.likes),
            joinedload(User.reviews).joinedload(NetworkReview.network)
        ).first())
        return users
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()


def createUser(ip: str, username: str):
    session = SessionLocal()

    try:
        session.add(User(ip_address=ip, username=username))
        session.commit()

        return "created"
    except Exception as e:
        print(e)
        session.rollback()

        return e
    finally:
        session.close()


def createLike(idUser: int, idNetwork: int):
    session = SessionLocal()

    try:
        session.add(NetworkLike(id_network=idNetwork, id_user=idUser))
        session.commit()

        return "created"
    except Exception as e:
        print(e)
        session.rollback()

        return e
    finally:
        session.close()


def createReview(review):
    session = SessionLocal()

    try:
        session.add(NetworkReview(id_network=review.id_network, id_user=review.id_user, text=review.text))
        session.commit()

        return "created"
    except Exception as e:
        print(e)
        session.rollback()

        return e
    finally:
        session.close()