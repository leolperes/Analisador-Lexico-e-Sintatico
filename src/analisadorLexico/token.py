# Grupo composto por:
# Leonardo Lemr Peres - Matriícula 23200521
#
# Arquivo de criação da classe token

class Token:
    def __init__(self, type, value, line, column):
        self.type = type
        self.value = value
        self.line = line
        self.column = column

    # Representação do token 
    def __repr__(self):
        return f"Token({self.type}, {self.value}, {self.line}, {self.column})"
