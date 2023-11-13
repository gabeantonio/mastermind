from mastermind import Mastermind
import requests
from colorama import Fore

def main():
    # Make a call to the API:
    hidden_combination = get_random_combination()
    # For testing:
    print('HIDDEN COMBINATION -->', hidden_combination)
    # Initialize a score variable:
    player_score = 0
    # Call the play game function:
    play_game(hidden_combination, player_score)

def play_game(hidden_combination: str, player_score: int):
    mastermind = Mastermind(hidden_combination)
    # Initialize game loop:
    while mastermind.continue_guessing():
        # Get user guess:
        user_guess = input('Type your guess here: ')
        # Input validation:
        if len(user_guess) < mastermind.COMBO_LENGTH:
            print(Fore.RED + f'Input too short. Please make sure your input is {mastermind.COMBO_LENGTH} digits long. \n' + Fore.RESET)
            continue
        elif len(user_guess) > mastermind.COMBO_LENGTH:
            print(Fore.RED + f'Input too long. Please make sure your input is only {mastermind.COMBO_LENGTH} long. \n' + Fore.RESET)
            continue
        
        # Add the user's guess to the guesses array:
        mastermind.add_guess(user_guess)
        # Pass the user guess into the check_guess function to return results regarding the user's guess:
        result = mastermind.check_guess(user_guess)
        correct_numbers, correct_positions, incorrect_numbers, correct_instances = result[0], result[1], result[2], result[3]

        # Show the user their past guesses:
        guesses = mastermind.view_guesses()
        # Show the user how many more guesses they have before the game ends:
        remaining_guesses = mastermind.remaining_guesses()

        # SCORE MANIPULATION:
        if correct_numbers == 0:
            hint_needed = input(Fore.RED + f'Sorry, those are all incorrect. Do you need a hint? Type Yes or No: ' + Fore.RESET)
            mastermind.hint(hint_needed)

        if correct_positions == 0:
            player_score += correct_instances
        elif correct_positions > 1:
            player_score += (correct_positions * 4) + correct_instances

        # FOR USER REFERENCE: THE AMOUNT OF GUESSES THEY HAVE LEFT AND THEIR PAST GUESSES:
        display_guesses(correct_numbers, correct_positions, player_score, remaining_guesses, guesses)

    # Winning logic:
    if mastermind.combination_found:
        print(Fore.GREEN + 'Congratulations! You have guessed the hidden combination correctly.' + Fore.RESET)
    else:
        print(Fore.RED +'You failed to guess the combination.')

def get_random_combination():
    api_url = "https://www.random.org/integers/?num=4&min=1&max=7&col=1&base=10&format=plain&rnd=new"
    response = requests.get(api_url)
    if response.status_code == 200:
        combination = ''
        combination += response.text
        # For some reason the text comes back in rows, so the below operation removes the spaces from the row:
        hidden_combination = combination.replace('\n', '')
        return hidden_combination
    else:
        print(f'Failed to get a random combination. Status code: {response.status_code}')

def display_guesses(correct_numbers: int, correct_positions: int, player_score: int, remaining_guesses: int, guesses: list):
    print(Fore.GREEN + f'You have guessed {correct_numbers} correct numbers and {correct_positions} correct positions.' + Fore.RESET)
    print(Fore.GREEN + f'Your score: {player_score}' + Fore.RESET)
    print(Fore.YELLOW + f'You have {remaining_guesses} remaining guesses.' + Fore.YELLOW)
    print(Fore.YELLOW + f'Your past guesses: {guesses} \n' + Fore.RESET)

if __name__ == '__main__':
    main()
