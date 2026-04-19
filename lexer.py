class Lexer:
    def __init__(self, input_text):
        self.input_text = input_text
        self.pos = 0

    def next_char(self):
        if self.pos < len(self.input_text):
            char = self.input_text[self.pos]
            self.pos += 1
            return char
        return None

    def retract(self):
        if self.pos > 0:
            self.pos -= 1

    def current_pos(self):
        return self.pos

    def set_pos(self, pos):
        self.pos = pos