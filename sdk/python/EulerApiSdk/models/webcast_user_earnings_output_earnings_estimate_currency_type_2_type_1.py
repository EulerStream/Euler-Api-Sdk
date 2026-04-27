from enum import Enum


class WebcastUserEarningsOutputEarningsEstimateCurrencyType2Type1(str, Enum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
