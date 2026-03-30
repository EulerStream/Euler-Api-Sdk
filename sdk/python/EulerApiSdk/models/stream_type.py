from enum import Enum


class StreamType(str, Enum):
    FLV_LD = "flv_ld"
    FLV_SD = "flv_sd"
    HLS_LD = "hls_ld"
    HLS_SD = "hls_sd"

    def __str__(self) -> str:
        return str(self.value)
