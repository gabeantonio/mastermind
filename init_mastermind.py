from mastermind import Mastermind
import requests
from colorama import Fore

def main():
    # MAKE API CALL AND STORE RETURNED COMBINATION IN THE BELOW VARIABLE:
    hidden_combination = get_random_combination()
    # FOR TESTING:
    print('HIDDEN COMBINATION: ', hidden_combination)
    # INITIALIZE THE PLAYER SCORE TO 0:
    player_score = 0
    # CALL THE PLAY GAME FUNCTION:
    play_game(hidden_combination, player_score)

def play_game(hidden_combination: str, player_score: int):
    # INSTANTIATE THE MASTERMIND CLASS:
    mastermind = Mastermind(hidden_combination)
    # INITIALIZE A WHILE LOOP TO CONTINUE LOOPING UNTIL THE MASTERMIND.CONTINUE_GUESSING FUNCTION IS STILL TRUE:
    while mastermind.continue_guessing():
        # GET THE USER'S GUESS:
        user_guess = input('Type your guess here: ')
        # WRITE LOGIC FOR USER INPUT VALIDATION:
        if len(user_guess) < mastermind.COMBO_LENGTH:
            print(Fore.RED + f'Input too short. Please make sure your input is {mastermind.COMBO_LENGTH} digits long. \n' + Fore.RESET)
            continue
        elif len(user_guess) > mastermind.COMBO_LENGTH:
            print(Fore.RED + f'Input too long. Please make sure your input is only {mastermind.COMBO_LENGTH} long. \n' + Fore.RESET)
            continue
        # ADD THE USER'S GUESS TO THE ARRAY OF PREVIOUS GUESSES:
        mastermind.add_guess(user_guess)
        # TAKE THE USER'S CURRENT GUESS AND CHECK TO SEE IF ANY ARE CORRECT:
        result = mastermind.check_guess(user_guess)
        # GIVE RESULT ELEMENTS PROPER VARIABLE NAMES:
        correct_numbers, correct_positions, correct_instances = result[0], result[1], result[2]
        # ALLOW USERS TO VIEW THEIR GUESSES AND REMAINING GUESSES:
        guesses = mastermind.view_guesses()
        remaining_guesses = mastermind.remaining_guesses()
        # WRITE SCORING LOGIC:
        # IF USER GUESSES NO CORRECT NUMBERS:
        if correct_numbers == 0:
            hint_needed = input(Fore.RED + f'Sorry, those are all incorrect. Do you need a hint? Type Yes or No: ' + Fore.RESET)
            mastermind.hint(hint_needed)
        # IF USER GUESSES SOME CORRECT NUMBERS:
        if correct_positions == 0:
            player_score += correct_instances
        # IF USER GUESSES A CORRECT NUMBER IN THE RIGHT POSITION:
        else:
            player_score += (correct_positions * 4) + correct_instances
        # AT EVERY ITERATION/GUESS, ALLOW THE USER TO SEE THEIR SCORES, THE NUMBER OF NUMBERS AND POSITIONS THEY GOT CORRECT, AS WELL AS THEIR REMAINING AND PREVIOUS GUESSES:
        display_guesses(correct_numbers, correct_positions, player_score, remaining_guesses, guesses)
    # WRITE WINNING LOGIC:
    if mastermind.combination_found:
        print(Fore.GREEN + 'Congratulations! You have guessed the hidden combination correctly.' + Fore.RESET)
    else:
        print(Fore.RED + f'You failed to guess the combination. The hidden combination was: {hidden_combination}')

def get_random_combination():
    api_url = "https://www.random.org/integers/?num=4&min=1&max=7&col=1&base=10&format=plain&rnd=new"
    response = requests.get(api_url)
    if response.status_code == 200:
        combination = ''
        combination += response.text
        # REPLACES ALL OF THE ROW SPACES WITH JUST ONE SPACE, MAKING THE RETURNED TEXT '1234' FORMAT:
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