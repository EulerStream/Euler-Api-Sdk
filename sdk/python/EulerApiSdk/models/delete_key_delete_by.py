from enum import Enum


class DeleteKeyDeleteBy(str, Enum):
    ID = "id"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)
