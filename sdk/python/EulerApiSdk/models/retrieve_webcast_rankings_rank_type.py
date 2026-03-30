from enum import Enum


class RetrieveWebcastRankingsRankType(str, Enum):
    DAILY_RANK = "DAILY_RANK"
    FANS_TEAM_RANK = "FANS_TEAM_RANK"

    def __str__(self) -> str:
        return str(self.value)
