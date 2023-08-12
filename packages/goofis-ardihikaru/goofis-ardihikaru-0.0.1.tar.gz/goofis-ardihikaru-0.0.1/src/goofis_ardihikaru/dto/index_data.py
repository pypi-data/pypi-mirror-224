from dataclasses import dataclass, asdict
from typing import Dict, Union

import simplejson as json


@dataclass
class General:
    """ General Data model """

    prev_price_close: float = 0.0

    day_range_min: float = 0.0
    day_range_max: float = 0.0
    day_range_diff: float = 0.0
    day_range_increase: bool = False

    year_range_min: float = 0.0
    year_range_max: float = 0.0
    year_range_diff: float = 0.0
    year_range_increase: bool = False


@dataclass
class IndexData:
    """ Index data model """

    general: General = General()
    about: str = ""
    current_price_change_percent: float = 0.0
    current_price_change_value: float = 0.0
    id: str = -1

    @staticmethod
    def sanitize(val: str) -> str:
        """ sanitizes json string """
        val = val.replace("'", '"')
        val = val.replace("False", 'false')
        val = val.replace("True", 'true')

        return val

    def val_to_dict(self, val: any) -> Union[None, int, str, Dict]:
        if val is None:
            return None
        if isinstance(val, int):
            return val
        if isinstance(val, str):
            return val

        val = str(val)

        # sanitizes
        val = self.sanitize(val)

        return json.loads(self.sanitize(val))

    def to_dict(self):
        return {
            k: self.val_to_dict(v) for k, v in asdict(self).items()
        }
