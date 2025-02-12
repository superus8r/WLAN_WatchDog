from dataclasses import dataclass

@dataclass
class KnownDevice:
    mac: str
    hint: str = ""

@dataclass
class Device:
    raw: str
    ip: str
    mac: str
    vendor: str = ""