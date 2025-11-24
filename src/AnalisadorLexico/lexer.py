# Grupo composto por:
# Leonardo Lemr Peres - Matriícula 23200521
#
# Arquivo do analisador léxico (lexer)


from __future__ import annotations
from typing import List, Optional
from .symbol_table import SymbolTable
from .token import Token


class Lexer:
    #-------------------------------PALAVRAS-CHAVE--------------------------------
    KEYWORDS = ["int", "if", "else", "def", "print", "return"]

    # Construtor
    def __init__(self, code: str):
        self.code = code
        self.pos = 0
        self.line = 1
        self.col = 1

        self.show_symbols = True

        # ----------- Tabela de símbolos ------------
        self.symbols = SymbolTable()

        # Inserir palavras-chave na tabela de símbolos
        for kw in self.KEYWORDS:
            self.symbols.insert(kw)

        self.tokens: List[Token] = []

    # ------------------------------------------------
    #                  UTILIDADES
    # ------------------------------------------------

    # Retorna o caractere atual sem avançar
    def peek(self) -> str:
        if self.pos >= len(self.code):
            return "\0"
        return self.code[self.pos]
    
    # Avança para o próximo caractere
    def advance(self):
        if self.pos < len(self.code):
            if self.code[self.pos] == '\n':
                self.line += 1
                self.col = 1
            else:
                self.col += 1
        self.pos += 1

    # Verifica se o próximo trecho do código corresponde ao esperado
    def match(self, expected: str) -> bool:
        if self.code[self.pos:self.pos+len(expected)] == expected:
            return True
        return False


    # ------------------------------------------------
    #                AFD: IDENTIFICADOR
    # ------------------------------------------------

    # Lê um identificador ou palavra-chave
    # Retorna o lexema ou None se não for um identificador
    def read_identifier(self) -> Optional[str]:
        if not self.peek().isalpha():
            return None

        lexeme = ""
        while self.peek().isalnum() or self.peek() == "_":
            lexeme += self.peek()
            self.advance()

        return lexeme

    # ------------------------------------------------
    #                   AFD: NÚMEROS
    # ------------------------------------------------

    # Lê um número
    # Retorna o lexema ou None se não for um número
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

    # Lê um operador ou símbolo
    # Retorna o token ou None se não for um operador/símbolo
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

    # Realiza a tokenização do código fonte
    # retorna uma lista de tokens
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
                if self.symbols.exists(ident):
                    token_type = ident.upper() if ident in self.KEYWORDS else "id"
                else:
                    self.symbols.insert(ident)
                    token_type = "id"
                self.tokens.append(Token(token_type, ident, start_line, start_col))
                continue

            # Números
            num = self.read_number()
            if num:
                if self.peek().isalpha() or self.peek() == "_":
                    print(f"Erro léxico: Identificador inválido começando com número '{num + self.peek()}' "
                          f"na linha {self.line}, coluna {self.col}")
                    self.show_symbols = False
                    break
                start_line = self.line
                start_col = self.col - len(num)
                self.tokens.append(Token("num", num, start_line, start_col))
                continue

            # Operadores e símbolos
            op = self.read_operator()
            if op:
                self.tokens.append(op)
                continue

            # Se nada reconheceu → erro léxico
            print(f"Erro léxico: Caractere inesperado '{c}' na linha {self.line}, coluna {self.col}")
            self.show_symbols = False
            break

        # Adicionar EOF no final
        self.tokens.append(Token("EOF", "$", self.line, self.col))



    # ------------------------------------------------
    #                   STRING
    # ------------------------------------------------

    # Representação em string dos tokens gerados
    def __str__(self) -> str:
        output = ""
        for t in self.tokens:
            output += f"{t}\n"
        return output


    #=------------------------------------------------
    #               GETTERS
    # ------------------------------------------------

    def get_tokens(self) -> List[Token]:
        return self.tokens