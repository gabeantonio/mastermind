class Mastermind:
    TOTAL_TRIES = 10
    COMBO_LENGTH = 4
    def __init__(self, hidden_combination: str):
        self.hidden_combination = hidden_combination
        self.guesses = []