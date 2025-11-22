from analisadorLexico import Lexer
from analisadorLexico import LexicalError

def main():

    code = """int x = 10;
    if (x > 5) return x;
    """

    lexer = Lexer(code)
    tokens = lexer.tokenize()


    print("===========================")
    print("----------Tokens:----------")
    print("===========================")

    for t in tokens:
        print(t)

    

    print(lexer.symbols.__str__())



if __name__ == "__main__":
    main()
