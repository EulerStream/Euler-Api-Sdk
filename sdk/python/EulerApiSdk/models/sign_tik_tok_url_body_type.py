from enum import Enum


class SignTikTokUrlBodyType(str, Enum):
    FETCH = "fetch"
    XHR = "xhr"

    def __str__(self) -> str:
        return str(self.value)
