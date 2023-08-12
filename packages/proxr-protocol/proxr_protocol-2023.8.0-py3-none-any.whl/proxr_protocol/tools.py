def calculate_checksum(data: bytes) -> bytes:
    cs = sum(data)
    cs &= 255
    return cs.to_bytes(1, "big")
