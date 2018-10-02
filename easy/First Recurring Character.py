class First_recurring_character:
    def __init__(self, input_str):
        self.str = input_str
    def find(self):
        if self.str == []:
            return None
        non_recurring_chars = []
        for char in self.str:
            if char not in non_recurring_chars:
                non_recurring_chars.append(char)
            else:
                return char
        return None
