class SymbolTable:
    def __init__(self):
        self.table = set()

    def insert(self, lexeme):
        self.table.add(lexeme)

    def exists(self, lexeme):
        return lexeme in self.table

    def __str__(self):
        print("\n===========================")
        print("----Tabela de Símbolos:----")
        print("===========================")
        output = ""
        for i, sym in enumerate(self.table):
            output += f"{i:03}  {sym}\n"
        return output
