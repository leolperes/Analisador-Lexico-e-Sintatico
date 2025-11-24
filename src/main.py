# Grupo composto por:
# Leonardo Lemr Peres - Matriícula 23200521
#
# Arquivo principal do programa


from AnalisadorLexico import Lexer
from AnalisadorSintatico import ParserPreditivo, ParseTable
from pathlib import Path

def main():
    # Solicita o nome do arquivo ao usuário
    filename = input("Digite o nome do arquivo de código a ser analisado: ").strip()

    root_path = Path(__file__).parent.parent
    file_path = root_path / filename

    try:
        # Lê o conteúdo do arquivo
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()



        # Cria o analisador léxico
        lexer = Lexer(code)
        lexer.tokenize()
        tokens = lexer.get_tokens()

        # verifica se deve exibir a tabela de símbolos e tokens
        if lexer.show_symbols:
            # Exibe os tokens gerados
            print("\n===========================")
            print("----------Tokens:----------:")
            print("===========================")
            print(lexer)

            # Exibe a tabela de símbolos
            print("\n===========================")
            print("----Tabela de Símbolos:----")
            print("===========================")
            print(lexer.symbols)

        

            # Cria o analisador sintático preditivo
            print("\n=============================")
            print("----Analisador Sintatico:----")
            print("=============================")
            parser = ParserPreditivo(tokens, ParseTable)
            parser.parse()



    # Trata erros de arquivo não encontrado
    except FileNotFoundError:
        print(f"Erro: Arquivo '{filename}' não encontrado.")


if __name__ == "__main__":
    main()
