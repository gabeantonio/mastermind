import random
from colorama import Fore

class Mastermind:
    TOTAL_TRIES = 10
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
        in_combination = []
        correct_positions = 0
        for i in range(len(self.hidden_combination)):
            number = user_guess[i]
            if number in self.hidden_combination:
                in_combination.append(number)
            if number == self.hidden_combination[i]:
                correct_positions += 1
        correct_numbers = len(set(in_combination))
        return [correct_numbers, correct_positions, len(in_combination)]
        
    # Write logic so that the user can view how many guesses they have left:
    def remaining_guesses(self):
        return self.TOTAL_TRIES - len(self.guesses)

    # Write logic that checks if a user can still make guesses:
    def continue_guessing(self):
        if self.TOTAL_TRIES - len(self.guesses) > 0 and self.combination_found == False:
            return True
        else: 
            return False
        
    # Write logic so that the user can get a hint if they need it:
    def hint(self, hint_needed: str):
        if hint_needed.lower() == 'yes':
            random_index = random.randint(0, len(self.hidden_combination) - 1)
            print(Fore.CYAN + f'\nOne of the numbers is {self.hidden_combination[random_index]}.\n' + Fore.RESET)
        elif hint_needed.lower() == 'no':
            print(Fore.GREEN + '\nOkay. Good luck!' + Fore.RESET)