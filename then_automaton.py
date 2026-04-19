from automaton import Automaton
from token import Token


class ThenAutomaton(Automaton):
    def recognize(self, lexer):
        start_pos = lexer.current_pos()
        target = "then"
        lexeme = ""

        for expected in target:
            char = lexer.next_char()
            if char == expected:
                lexeme += char
            else:
                lexer.set_pos(start_pos)
                return None

        char = lexer.next_char()

        if char is None or not char.isalnum():
            if char is not None:
                lexer.retract()
            return Token("THEN", lexeme)
        else:
            lexer.set_pos(start_pos)
            return None