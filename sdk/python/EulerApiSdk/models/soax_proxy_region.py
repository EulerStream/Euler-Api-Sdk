from enum import Enum


class SoaxProxyRegion(str, Enum):
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    PL = "PL"

    def __str__(self) -> str:
        return str(self.value)
