from . import tools


def bank_invert(bank: int) -> bytes:
    out = b"\xAA"
    out += b"\x03"  # number of data bytes
    out += b"\xFE"
    out += b"\x83"
    out += bank.to_bytes(1, "big")  # bank index
    out += tools.calculate_checksum(out)
    return out


def bank_off(bank: int) -> bytes:
    out = b"\xAA"
    out += b"\x03"  # number of data bytes
    out += b"\xFE"
    out += b"\x81"
    out += bank.to_bytes(1, "big")  # bank index
    out += tools.calculate_checksum(out)
    return out


def bank_on(bank: int) -> bytes:
    out = b"\xAA"
    out += b"\x03"  # number of data bytes
    out += b"\xFE"
    out += b"\x82"
    out += bank.to_bytes(1, "big")  # bank index
    out += tools.calculate_checksum(out)
    return out


def bank_reverse(bank: int) -> bytes:
    out = b"\xAA"
    out += b"\x03"  # number of data bytes
    out += b"\xFE"
    out += b"\x84"
    out += bank.to_bytes(1, "big")  # bank index
    out += tools.calculate_checksum(out)
    return out
