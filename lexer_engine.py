from lexer import Lexer
from identifier_automaton import IdentifierAutomaton
from then_automaton import ThenAutomaton


class LexerEngine:
    def __init__(self, input_text):
        self.lexer = Lexer(input_text)

        # Orden = prioridad
        self.automata = [
            ThenAutomaton(),
            IdentifierAutomaton()
        ]

    def tokenize(self):
        tokens = []

        while self.lexer.current_pos() < len(self.lexer.input_text):

            char = self.lexer.next_char()

            if char is not None and char.isspace():
                continue

            self.lexer.retract()

            token = None

            for automaton in self.automata:
                token = automaton.recognize(self.lexer)
                if token:
                    tokens.append(token)
                    break

            if not token:
                error_char = self.lexer.next_char()
                print(f"Error léxico en: '{error_char}'")

        return tokens