from lexer.lexer import Lexer

def main():
    # Apenas um código qualquer para inicializar o lexer
    sample_code = "int x = 10;"

    # Instancia o lexer
    lexer = Lexer(sample_code, token_file="tokens.json")

    # AQUI testamos a função compile_regex
    print("\n--- Testando compile_regex ---")
    for token_type, regex in lexer.token_regex:
        print(f"{token_type} -> {regex.pattern}")

if __name__ == "__main__":
    main()
