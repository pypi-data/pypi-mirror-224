from dataclasses import dataclass, asdict


@dataclass
class ServiceId:
    """ Service ID object """

    service_id: str

    def to_dict(self):
        return {k: str(v) for k, v in asdict(self).items()}
