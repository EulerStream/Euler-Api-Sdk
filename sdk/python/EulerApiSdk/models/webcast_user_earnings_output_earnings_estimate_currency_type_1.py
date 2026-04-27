from enum import Enum


class WebcastUserEarningsOutputEarningsEstimateCurrencyType1(str, Enum):
    USD = "USD"

    def __str__(self) -> str:
        return str(self.value)
