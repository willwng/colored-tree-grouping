from __future__ import annotations

from enum import Enum
from typing import List
import random


def get_all_protocols() -> List[Protocol]:
    return [Protocol.MPC, Protocol.ABY, Protocol.WIL, Protocol.VIV, Protocol.SAM, Protocol.COM]


def get_random_protocol() -> Protocol:
    return random.choice(get_all_protocols())


class Protocol(Enum):
    MPC = 1
    ABY = 2
    WIL = 3
    VIV = 4
    SAM = 5
    COM = 6

    def __str__(self):
        return self.name

    def to_color(self) -> str:
        if self == Protocol.MPC:
            return "red"
        elif self == Protocol.ABY:
            return "blue"
        elif self == Protocol.WIL:
            return "green"
        else:
            return "black"
