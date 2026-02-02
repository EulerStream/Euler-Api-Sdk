from enum import IntEnum


class MuteDuration(IntEnum):
    VALUE_NEGATIVE_1 = -1
    VALUE_5 = 5
    VALUE_30 = 30
    VALUE_60 = 60
    VALUE_300 = 300

    def __str__(self) -> str:
        return str(self.value)
