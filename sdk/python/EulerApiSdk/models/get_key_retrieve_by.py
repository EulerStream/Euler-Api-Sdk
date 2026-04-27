from enum import Enum


class GetKeyRetrieveBy(str, Enum):
    ID = "id"
    VALUE = "value"

    def __str__(self) -> str:
        return str(self.value)
