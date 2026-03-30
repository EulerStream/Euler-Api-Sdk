from enum import IntEnum


class AlertTargetStatus(IntEnum):
    VALUE_0 = 0
    VALUE_1 = 1
    VALUE_4 = 4

    def __str__(self) -> str:
        return str(self.value)
