# Grupo composto por:
# Leonardo Lemr Peres - Matriícula 23200521
#
# Arquivo de criação da classe tabela de símbolos

class SymbolTable:
    def __init__(self):
        self.table = set()

    # Insere um novo lexema na tabela de símbolos
    def insert(self, lexeme):
        self.table.add(lexeme)

    # Verifica se o lexema existe na tabela de símbolos
    def exists(self, lexeme):
        return lexeme in self.table

    # Representação em string da tabela de símbolos
    def __str__(self):
        output = ""
        for i, sym in enumerate(self.table):
            output += f"{i:03}  {sym}\n"
        return output
