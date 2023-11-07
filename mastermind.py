class Mastermind:
    TOTAL_TRIES = 10
    COMBO_LENGTH = 4
    def __init__(self, hidden_combination: str):
        self.hidden_combination = hidden_combination
        self.guesses = []

    # Write winning logic:
    def combination_found(self):
        if self.guesses[-1] == self.hidden_combination:
            return True
        else: 
            False

    # Write logic in the event that a user attempts a combination:
    