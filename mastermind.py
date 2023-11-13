import random
from colorama import Fore

class Mastermind:
    TOTAL_TRIES = 10
    COMBO_LENGTH = 4
    def __init__(self, hidden_combination: str):
        self.hidden_combination = hidden_combination
        self.guesses = []

    # Write winning logic:
    # Make it a property so it doesnt get called before you can input anything.
    @property
    def combination_found(self):
        if len(self.guesses) > 0 and self.guesses[-1] == self.hidden_combination:
            return True
        else: 
            return False

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
        in_combination = []
        correct_position = 0
        for number in user_guess:
            guessed_combination.append(number)
        guessed_numbers = set(guessed_combination)
        for i in range(self.COMBO_LENGTH):
            number = user_guess[i]
            if number not in self.hidden_combination:
                incorrect_numbers.append(number)
            else:
                in_combination.append(number)

            if number == self.hidden_combination[i]:
                correct_position += 1
        wrong_numbers = set(incorrect_numbers)
        correct_numbers = len(guessed_numbers) - len(wrong_numbers)
        # Add in_combination to return statement. in_combination will hold the number of correct numbers INCLUDING DUPLICATES,
        # which is helpful when adding 1 extra point for each correct number in a correct position (duplicates weren't being accounted for in this case).
        return [correct_numbers, correct_position, len(in_combination)]
        
    # Write logic so that the user can view how many guesses they have left:
    def remaining_guesses(self):
        return self.TOTAL_TRIES - len(self.guesses)

    # Write logic that checks if a user can still make guesses:
    def continue_guessing(self):
        if self.TOTAL_TRIES - len(self.guesses) > 0 and not self.combination_found:
            return True
        else: 
            return False
        
    # Write logic so that the user can get a hint if they need it:
    def hint(self, hint_needed: str):
        if hint_needed.lower() == 'yes':
            random_index = random.randint(0, 3)
            print(Fore.CYAN + f'\nOne of the numbers is {self.hidden_combination[random_index]}.\n' + Fore.RESET)
        elif hint_needed.lower() == 'no':
            print(Fore.GREEN + '\nOkay. Good luck!' + Fore.RESET)