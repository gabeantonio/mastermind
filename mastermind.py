class Mastermind:
    TOTAL_TRIES = 10
    COMBO_LENGTH = 4
    def __init__(self, hidden_combination: str):
        self.hidden_combination = hidden_combination
        self.guesses = []

    # Write winning logic:
    def combination_found(self):
        if len(self.guesses) > 0 and self.guesses[-1] == self.hidden_combination:
            return True
        else: 
            False

    # Write logic in the event that a user attempts a combination:
    def add_guess(self, combination: str):
        self.guesses.append(combination)

    # Write logic for a user to be able to view their past guesses:
    def view_guesses(self):
        return self.guesses
    
    # Write logic that checks if the guess is correct, partially correct, or incorrect:
    def check_guess(self):
        pass

    # Write logic that checks if a user can still make guesses:
    def continue_guessing(self):
        if self.TOTAL_TRIES - len(self.guesses) > 0 and not self.combination_found:
            return True