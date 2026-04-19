from lexer_engine import LexerEngine


def main():
    user_input = input("Ingrese la cadena a analizar: ")

    engine = LexerEngine(user_input)
    tokens = engine.tokenize()

    print("\nTokens encontrados:")
    for t in tokens:
        print(t)


if __name__ == "__main__":
    main()