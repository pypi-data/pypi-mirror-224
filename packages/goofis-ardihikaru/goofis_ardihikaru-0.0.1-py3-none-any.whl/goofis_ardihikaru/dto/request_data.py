from dataclasses import dataclass


@dataclass
class RequestData:
    """ Http Request data model """

    authorized: bool
    id: str = -1
