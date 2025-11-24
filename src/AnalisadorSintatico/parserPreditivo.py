# Grupo composto por:
# Leonardo Lemr Peres - Matriícula 23200521
#
# Arquivo do analisador sintático preditivo

from __future__ import annotations
from typing import List, Tuple, Dict

from AnalisadorLexico.token import Token


# Analisador Sintático Preditivo
class ParserPreditivo:

    # Construtor
    def __init__(self, tokens: List[Token], parse_table: Dict[Tuple[str, str], List[str]]):
        self.tokens = tokens
        self.table = parse_table
        self.position = 0
        self.stack = ["$", "MAIN"]

    # Retorna o token atual
    def current_token(self) -> Token:
        return self.tokens[self.position]

    # Avança para o próximo token
    def advance(self):
        if self.position < len(self.tokens) - 1:
            self.position += 1


    # Realiza a análise sintática preditiva
    def parse(self):
        while len(self.stack) > 0:
            top = self.stack.pop()
            current = self.current_token()

            # Caso final
            if top == "$":
                if current.type == "EOF":
                    print("✓ Análise sintática concluída sem erros.")
                    return
                else:
                    print(f"Erro sintático: esperado EOF, encontrado {current.type}")
                    return

            # Caso terminal
            if self.is_terminal(top):
                if top == current.type or top == current.value:
                    self.advance()
                else:
                    print(
                        f"Erro sintático: esperado '{top}', encontrado '{current.value}' "
                        f"(linha {current.line}, coluna {current.column})"
                    )
                    return
                continue

            # Não terminal → busca regra na tabela
            key = (top, current.type)

            if key not in self.table:
                key = (top, current.value)

            if key not in self.table:
                print(
                    f"Erro sintático: nenhuma regra para ({top}, {current.value}) "
                    f"na linha {current.line}, coluna {current.column}"
                )
                return

            production = self.table[key]

            # Produção vazia
            if production == ["ε"]:
                continue

            # Empilha produção em ordem reversa
            for symbol in reversed(production):
                self.stack.append(symbol)

        # Pilha acabou mas ainda há tokens
        if self.current_token().type != "EOF":
            t = self.current_token()
            print(
                f"Erro sintático: sobrou token inesperado '{t.value}' "
                f"(linha {t.line}, coluna {t.column})"
            )
            return

    def is_terminal(self, symbol: str) -> bool:
        terminals = {
            "id", "num", "def", "if", "else", "int",
            "print", "return", "+", "-", "*", "/", "(", ")",
            "{", "}", ",", ";", "<", "<=", ">", ">=", "==", "!=",
            "=", "$"
        }
        return symbol in terminals
