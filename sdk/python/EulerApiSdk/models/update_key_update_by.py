from enum import Enum


class UpdateKeyUpdateBy(str, Enum):
    ID = "id"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)
