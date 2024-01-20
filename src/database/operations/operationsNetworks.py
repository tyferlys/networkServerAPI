from sqlalchemy.orm import joinedload

from src.database.database import SessionLocal
from src.database.models.Network import Network, NetworkReview
from src.database.models.NetworkLike import NetworkLike


def getAllNetworks():
    session = SessionLocal()

    try:
        networks = (session.query(Network).options(joinedload(Network.tags))
                    .options(joinedload(Network.likes))
                    .all())
        return networks
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()


def getNetwork(idNetwork: int):
    session = SessionLocal()

    try:
        network = (session.query(Network).where(Network.id == idNetwork).options(
            joinedload(Network.tags),
            joinedload(Network.likes),
            joinedload(Network.reviews).joinedload(NetworkReview.user)
        ).first())

        return network
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()

