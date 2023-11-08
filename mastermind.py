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
    def check_guess(self, user_guess: str):
        guessed_combination = []
        incorrect_numbers = []
        correct_numbers = 0
        correct_position = 0
        for number in user_guess:
            guessed_combination.append(number)
        guessed_numbers = set(guessed_combination)
        for i in range(self.COMBO_LENGTH):
            number = user_guess[i]
            if number not in self.hidden_combination:
                incorrect_numbers.append(number)
            if number == self.hidden_combination[i]:
                correct_position += 1
        wrong_numbers = set(incorrect_numbers)
        correct_numbers = len(guessed_numbers) - len(wrong_numbers)
        return [correct_numbers, correct_position]
        
    # Write logic that checks if a user can still make guesses:
    def continue_guessing(self):
        if self.TOTAL_TRIES - len(self.guesses) > 0 and not self.combination_found:
            return True