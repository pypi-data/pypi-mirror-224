import base64
import io
import math
import os
from dataclasses import dataclass
from typing import Dict, Optional

import emoji
from cryptography.fernet import Fernet

ByteMapping = Dict[bytes, str]
InverseByteMapping = Dict[str, bytes]


def generate_key():
    key_base = os.urandom(4)
    return key_base, base64.urlsafe_b64encode(key_base * 8)


MOJIPACK_VERSION = 1
SIGNATURE = "#MOJI".encode("ascii")
DEFAULT_KEY_BASE, DEFAULT_KEY = generate_key()

ZW_SPACE = "\u200c"


def encode_unsigned_short(n: int) -> bytes:
    if not 0 <= n <= 65535:
        raise ValueError("Value out of range for unsigned short")

    return n.to_bytes(2, byteorder="big")


def decode_unsigned_short(b: bytes) -> int:
    if len(b) != 2:
        raise ValueError("Invalid bytes length for unsigned short")

    return int.from_bytes(b, byteorder="big")


def make_header(key_base: bytes):
    assert len(key_base) == 4

    with io.BytesIO() as header_buf:
        header_buf.write(SIGNATURE)
        header_buf.write(encode_unsigned_short(MOJIPACK_VERSION))
        header_buf.write(key_base)

        header_data = header_buf.getvalue()

    return header_data


EXAMPLE_HEADER = make_header(b"aaaa")


@dataclass
class MojiEncodeOptions:
    line_width: int = -1


@dataclass
class MojiDecodeOptions:
    ...


class MojiCodec:
    byte_mapping: ByteMapping
    inverse_byte_mapping: InverseByteMapping

    def __init__(self, byte_mapping: ByteMapping):
        self.byte_mapping = byte_mapping
        self.inverse_byte_mapping = {v: k for k, v in byte_mapping.items()}

    def encode_byte(self, b: bytes) -> str:
        try:
            return self.byte_mapping[b]

        except KeyError as e:
            print(b, type(b))
            raise e

    def decode_emoji(self, e: str) -> bytes:
        return self.inverse_byte_mapping[e]

    def encode(self, b: bytes, options: Optional[MojiEncodeOptions] = None) -> str:
        lines = []
        options = options or MojiEncodeOptions()

        if options.line_width < 0:
            line_width = min(40, math.ceil(math.sqrt(len(b) + len(EXAMPLE_HEADER)) * 1.5))

        else:
            line_width = options.line_width

        key_base, key = generate_key()
        header_data = make_header(key_base)
        cipher_suite = Fernet(key)

        with io.BytesIO(header_data + cipher_suite.encrypt(b)) as buf:
            line = []

            while a_single_byte := buf.read(1):
                line.append(self.encode_byte(a_single_byte))

                if len(line) >= line_width:
                    lines.append(ZW_SPACE.join(line))
                    line = []

            if line:
                lines.append(ZW_SPACE.join(line))

        return os.linesep.join(lines)

    def decode(self, s: str, options: Optional[MojiDecodeOptions] = None):
        _ = options or MojiDecodeOptions()

        with io.BytesIO() as buf:
            for e in emoji.analyze(s, join_emoji=True, non_emoji=False):
                buf.write(self.decode_emoji(e.chars))

            buf.seek(0)

            signature = buf.read(len(SIGNATURE))
            assert signature == SIGNATURE

            version = decode_unsigned_short(buf.read(2))
            assert version == MOJIPACK_VERSION

            key_base = buf.read(len(DEFAULT_KEY_BASE))

            cipher_suite = Fernet(base64.urlsafe_b64encode(key_base * 8))

            data = cipher_suite.decrypt(buf.read())

        return data
