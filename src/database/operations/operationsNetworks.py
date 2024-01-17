from sqlalchemy.orm import joinedload

from src.database.database import SessionLocal
from src.database.models.Network import Network


def getAllNetworks():
    session = SessionLocal()

    try:
        networks = session.query(Network).options(joinedload(Network.tags)).all()
        return networks
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()


def getNetwork(idNetwork: int):
    session = SessionLocal()

    try:
        network = session.query(Network).options(joinedload(Network.tags)).where(Network.id == idNetwork).first()
        return network
    except Exception as e:
        print(e)
        return e
    finally:
        session.close()
