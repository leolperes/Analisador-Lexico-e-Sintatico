from __future__ import annotations
from typing import List, Optional
from .errors import LexicalError
from .symbol_table import SymbolTable
from .token import Token


class Lexer:
    KEYWORDS = ["int", "if", "else", "def", "print", "return"]

    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.line = 1
        self.col = 1

        # ----------- Tabela de símbolos ------------
        self.symbols = SymbolTable()

        # Inserir palavras-chave na tabela de símbolos
        for kw in self.KEYWORDS:
            self.symbols.insert(kw)

        self.tokens: List[Token] = []

    # ------------------------------------------------
    #                  UTILIDADES
    # ------------------------------------------------
    def peek(self) -> str:
        if self.pos >= len(self.code):
            return "\0"
        return self.code[self.pos]

    def advance(self):
        if self.pos < len(self.code):
            if self.code[self.pos] == '\n':
                self.line += 1
                self.col = 1
            else:
                self.col += 1
        self.pos += 1

    def match(self, expected: str) -> bool:
        if self.code[self.pos:self.pos+len(expected)] == expected:
            return True
        return False

    # ------------------------------------------------
    #                DFA: IDENTIFICADOR
    # ------------------------------------------------
    def read_identifier(self) -> Optional[str]:
        if not self.peek().isalpha():
            return None

        lexeme = ""
        while self.peek().isalnum() or self.peek() == "_":
            lexeme += self.peek()
            self.advance()

        return lexeme

    # ------------------------------------------------
    #                   DFA: NÚMEROS
    # ------------------------------------------------
    def read_number(self) -> Optional[str]:
        if not self.peek().isdigit():
            return None

        lexeme = ""
        while self.peek().isdigit():
            lexeme += self.peek()
            self.advance()

        return lexeme

    # ------------------------------------------------
    #             OPERADORES E SÍMBOLOS
    # ------------------------------------------------
    def read_operator(self) -> Optional[Token]:
        c = self.peek()

        if c == "\0":
            return None

        start_line = self.line
        start_col = self.col

        # Operadores de dois caracteres
        if self.match("<="):
            self.advance(); self.advance()
            return Token("LE", "<=", start_line, start_col)
        if self.match(">="):
            self.advance(); self.advance()
            return Token("GE", ">=", start_line, start_col)
        if self.match("=="):
            self.advance(); self.advance()
            return Token("EQ", "==", start_line, start_col)
        if self.match("!="):
            self.advance(); self.advance()
            return Token("NE", "!=", start_line, start_col)

        # Operadores simples
        single = {
            '+': "PLUS",
            '-': "MINUS",
            '*': "MULT",
            '/': "DIV",
            '<': "LT",
            '>': "GT",
            '=': "ASSIGN",
            '(': "LPAREN",
            ')': "RPAREN",
            '{': "LBRACE",
            '}': "RBRACE",
            ',': "COMMA",
            ';': "SEMICOLON",
        }

        if c in single:
            token_type = single[c]
            self.advance()
            return Token(token_type, c, start_line, start_col)

        return None

    # ------------------------------------------------
    #                   TOKENIZAÇÃO
    # ------------------------------------------------
    def tokenize(self) -> List[Token]:
        while self.pos < len(self.code):

            c = self.peek()

            # Espaços e quebras de linha
            if c.isspace():
                self.advance()
                continue

            # Identificadores / Palavras-chave
            ident = self.read_identifier()
            if ident:
                start_line = self.line
                start_col = self.col - len(ident)

                # Agora usamos a tabela de símbolos
                if self.symbols.exists(ident):

                    # Se está entre as palavras-chave → KEYWORD
                    if ident in self.KEYWORDS:
                        self.tokens.append(Token(ident.upper(), ident, start_line, start_col))

                    else:
                        # Identificador já existente
                        self.tokens.append(Token("ID", ident, start_line, start_col))

                else:
                    # Identificador novo → inserir na tabela
                    self.symbols.insert(ident)
                    self.tokens.append(Token("ID", ident, start_line, start_col))

                continue

            # Números
            num = self.read_number()
            if num:
                start_line = self.line
                start_col = self.col - len(num)
                self.tokens.append(Token("NUM", num, start_line, start_col))
                continue

            # Operadores e símbolos
            op = self.read_operator()
            if op:
                self.tokens.append(op)
                continue

            # Se nada reconheceu → erro léxico
            raise LexicalError(
                f"Caractere inesperado '{c}' na linha {self.line}, coluna {self.col}"
            )

        self.tokens.append(Token("EOF", "", self.line, self.col))
        return self.tokens

    # ------------------------------------------------
    #                   STRING
    # ------------------------------------------------
    def __str__(self) -> str:
        output = "===========================\n"
        output += "----------Tokens:----------\n"
        output += "===========================\n"
        for t in self.tokens:
            output += f"{t}\n"
        return output
