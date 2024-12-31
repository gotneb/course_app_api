from dataclasses import dataclass


@dataclass
class Instructor:
    id: int
    name: str
    profile_url: str