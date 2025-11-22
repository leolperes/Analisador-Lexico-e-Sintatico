from __future__ import annotations
import json
import re
from pathlib import Path
from typing import List, Optional, Tuple


from .token import Token
from .errors import LexicalError


class Lexer:
    def __init__(self, code: str, token_file: str = "tokens.json"):
        self.code = code
        self.position = 0
        self.line = 1
        self.column = 1
        self.tokens: List[Token] = []


        self.token_file = token_file
        self.token_defs = self.load_tokens(token_file)
        self.token_regex = self.compile_regex(self.token_defs)


    def load_tokens(self, filepath: str) -> List[dict]:
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"Token definition file not found: {filepath}")
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)


    def compile_regex(self, token_defs: List[dict]) -> List[Tuple[str, re.Pattern]]:
        regex_list = []
        for t in token_defs:
            try:
                pattern = re.compile(t["regex"])
            except re.error as e:
                raise LexicalError(f"Invalid regex for token {t['type']}: {e}")
            regex_list.append((t["type"], pattern))
        return regex_list


    def peek(self, length: int = 1) -> str:
        return self.code[self.position:self.position + length]


    def advance(self, length: int = 1):
        for _ in range(length):
            if self.position < len(self.code):
                if self.code[self.position] == '\n':
                    self.line += 1
                    self.column = 1
                else:
                    self.column += 1
                self.position += 1


    def tokenize(self) -> List[Token]:
        while self.position < len(self.code):
            match_found = False


            for token_type, pattern in self.token_regex:
                match = pattern.match(self.code, self.position)
                if match:
                    value = match.group(0)


                    if token_type != "WHITESPACE":
                        self.tokens.append(Token(token_type, value, self.line, self.column))


                    self.advance(len(value))
                    match_found = True
                    break


            if not match_found:
                char = self.peek()
                raise LexicalError(f"Unexpected character '{char}' at line {self.line}, column {self.column}")


        self.tokens.append(Token("EOF", None, self.line, self.column))
        return self.tokens