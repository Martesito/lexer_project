from automaton import Automaton
from token import Token


class IdentifierAutomaton(Automaton):
    def recognize(self, lexer):
        start_pos = lexer.current_pos()
        state = 9
        lexeme = ""

        while True:
            char = lexer.next_char()

            if state == 9:
                if char is not None and char.isalpha():
                    state = 10
                    lexeme += char
                else:
                    lexer.set_pos(start_pos)
                    return None

            elif state == 10:
                if char is not None and char.isalnum():
                    lexeme += char
                else:
                    if char is not None:
                        lexer.retract()
                    return Token("ID", lexeme)