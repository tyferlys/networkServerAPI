from typing import List

from fastapi import APIRouter

from src.database.operations.operationsNetworks import getAllNetworks
from src.types.NetworksDataResponse import NetworksDataResponse

routerNetworks = APIRouter()


@routerNetworks.get("/")
def data_networks() -> List[NetworksDataResponse]:
    networks = getAllNetworks()

    return networks
