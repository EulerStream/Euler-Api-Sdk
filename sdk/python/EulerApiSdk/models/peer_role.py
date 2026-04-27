from enum import Enum


class PeerRole(str, Enum):
    ENTERPRISE = "enterprise"
    PUBLIC = "public"
    STAGING = "staging"

    def __str__(self) -> str:
        return str(self.value)
