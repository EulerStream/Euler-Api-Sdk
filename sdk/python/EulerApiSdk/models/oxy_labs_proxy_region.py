from enum import Enum


class OxyLabsProxyRegion(str, Enum):
    AR = "AR"
    AU = "AU"
    BE = "BE"
    BR = "BR"
    CA = "CA"
    CL = "CL"
    CO = "CO"
    DE = "DE"
    ES = "ES"
    FR = "FR"
    GB = "GB"
    IT = "IT"
    JP = "JP"
    KR = "KR"
    MX = "MX"
    PE = "PE"
    PL = "PL"
    RO = "RO"
    SG = "SG"
    US = "US"

    def __str__(self) -> str:
        return str(self.value)
