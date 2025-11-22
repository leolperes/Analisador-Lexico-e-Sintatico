from dataclasses import dataclass

@dataclass
class Token:
    type: str
    value: str | None
    line: int
    column: int

    def __repr__(self):
        return f"Token({self.type!r}, {self.value!r}, line={self.line}, col={self.column})"

