from enum import Enum


class WebcastUserEarningsOutputPeriod(str, Enum):
    DAILY = "daily"

    def __str__(self) -> str:
        return str(self.value)
