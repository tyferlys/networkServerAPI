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
