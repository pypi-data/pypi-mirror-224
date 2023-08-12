from dataclasses import dataclass


@dataclass(frozen=True)
class AccountName:
    name: str
