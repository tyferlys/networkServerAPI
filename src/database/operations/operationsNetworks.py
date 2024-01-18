from sqlalchemy.orm import joinedload

from src.database.database import SessionLocal
from src.database.models.Network import Network
from src.database.models.NetworkLike import NetworkLike
from src.database.models.NetworkReview import NetworkReview


def getAllNetworks():
    session = SessionLocal()

    try:
        networks = (session.query(Network).options(joinedload(Network.tags))
                    .options(joinedload(Network.likes)).all())
        return networks
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()


def getNetwork(idNetwork: int):
    session = SessionLocal()

    try:
        network = (session.query(Network).options(joinedload(Network.tags))
                   .options(joinedload(Network.likes))
                   .where(Network.id == idNetwork).first())

        return network
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()


def getReviewForNetwork(idNetwork: int):
    session = SessionLocal()

    try:
        reviews = (session.query(NetworkReview)
                   .where(NetworkReview.id_network == idNetwork).all())

        return reviews
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()