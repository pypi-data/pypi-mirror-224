from . import tools


def relay_off(relay: int) -> bytes:
    """Relay is zero indexed."""
    assert 1 <= relay <= 65535
    out = b"\xAA"
    out += b"\x04"  # number of data bytes
    out += b"\xFE"
    out += b"\x2F"
    out += relay.to_bytes(2, "big")[::-1]  # relay index
    out += tools.calculate_checksum(out)
    print(out)
    return out


def relay_off_by_bank(relay: int, bank: int) -> bytes:
    """Relay and bank are 1-indexed. If bank is zero command will apply to all banks."""
    assert 1 <= relay <= 8
    out = b"\xAA"
    out += b"\x03"  # number of data bytes
    out += b"\xFE"
    out += (0x63 + relay).to_bytes(1, "big")  # relay index
    out += bank.to_bytes(1, "big")  # bank index
    out += tools.calculate_checksum(out)
    return out


def relay_on(relay: int) -> bytes:
    """Relay is zero indexed."""
    assert 1 <= relay <= 65535
    out = b"\xAA"
    out += b"\x04"  # number of data bytes
    out += b"\xFE"
    out += b"\x30"
    out += relay.to_bytes(2, "big")[::-1]  # relay index
    out += tools.calculate_checksum(out)
    print(out)
    return out


def relay_on_by_bank(relay: int, bank: int) -> bytes:
    """Relay and bank are 1-indexed. If bank is zero command will apply to all banks."""
    assert 1 <= relay <= 8
    out = b"\xAA"
    out += b"\x03"  # number of data bytes
    out += b"\xFE"
    out += (0x6B + relay).to_bytes(1, "big")  # relay index
    out += bank.to_bytes(1, "big")  # bank index
    out += tools.calculate_checksum(out)
    return out


def relay_read_status(relay: int) -> bytes:
    """Relay is zero indexed."""
    assert 1 <= relay <= 65535
    out = b"\xAA"
    out += b"\x04"  # number of data bytes
    out += b"\xFE"
    out += b"\x2C"
    out += relay.to_bytes(2, "big")[::-1]  # relay index
    out += tools.calculate_checksum(out)
    print(out)
    return out
