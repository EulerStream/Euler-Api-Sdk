from enum import Enum


class PeerPresenceType(str, Enum):
    AGENT = "agent"
    API = "api"

    def __str__(self) -> str:
        return str(self.value)
