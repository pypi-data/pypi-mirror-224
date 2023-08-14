from typing import Optional

from mojipack.codec import MojiEncodeOptions, MojiCodec, MojiDecodeOptions
from mojipack.default_byte_mapping import DEFAULT_BYTE_MAPPING

__version__ = "1.0.0"
version = __version__
DEFAULT_CODEC = MojiCodec(DEFAULT_BYTE_MAPPING)


def encode(b: bytes, options: Optional[MojiEncodeOptions] = None) -> str:
    return DEFAULT_CODEC.encode(b, options)


def decode(s: str, options: Optional[MojiDecodeOptions] = None):
    return DEFAULT_CODEC.decode(s, options)


__all__ = [
    "version",
    "encode",
    "decode",
    "MojiCodec",
    "MojiEncodeOptions",
    "MojiDecodeOptions"
]
