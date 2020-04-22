import json
from dataclasses import dataclass

@dataclass(frozen=True)
class DealResponse:
    text: str
    response_type: str = 'in_channel'
