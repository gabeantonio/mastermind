from mastermind import Mastermind
import requests
from colorama import Fore
import random


def main():
    # Make a call to the API:
    api_url = "https://www.random.org/integers/?num=4&min=1&max=7&col=1&base=10&format=plain&rnd=new"
    response = requests.get(api_url)
    if response.status_code == 200:
        combination = ''
        combination += response.text
        # For some reason the text comes back in rows, so the below operation removes the spaces from the row:
        hidden_combination = combination.replace('\n', '')
    else:
        print(f'Failed to get a random combination. Status code: {response.status_code}')
    
    print('HIDDEN COMBINATION -->', hidden_combination)

    play_game(hidden_combination)


def play_game(hidden_combination: str):
    mastermind = Mastermind(hidden_combination)
    # Initialize a score variable:
    player_score = 0
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
        # Check if user's guess is has any correct numbers and positions:
        check = mastermind.check_guess(user_guess)
        # Show the user their past guesses:
        guesses = mastermind.view_guesses()
        # Show the user how many more guesses they have before the game ends:
        remaining_guesses = mastermind.remaining_guesses()

        # Check if the guess is partially correct or completely incorrect.
        # All wrong:
        if check[0] == 0 and check[1] == 0:
            if player_score >= 4:
                player_score -= 4
            elif player_score >= 1:
                player_score -= 1
            else:
                player_score -= 0
            print(Fore.RED + f'Sorry, all are incorrect.' + Fore.RESET)
            print(Fore.RED + f'Your score decreased! Your score: {player_score}' + Fore.RESET)
            # HINT: 
            hint_needed = input('Do you need a hint? Type Yes or No: ')
            if hint_needed.lower() == 'yes':
                random_index = random.randint(0, 3)
                print(f'One of the numbers is {hidden_combination[random_index]}.')
            elif hint_needed.lower() == 'no':
                print('Okay. Good luck!')
        # No right positions:
        elif check[1] == 0:
            # Some correct numbers and some incorrect numbers present:
            if check[0] > 0 and check[2] > 0:
                player_score += check[0] - check[2]
            # Correct numbers present but not in right position:
            else:
                player_score += 4
            print(Fore.GREEN + f'You have guessed {check[0]} correct numbers and {check[1]} correct positions. STATEMENT 1' + Fore.RESET)
            print(Fore.GREEN + f'Your score: {player_score}' + Fore.RESET)
        # Right positions:
        elif check[1] > 0:
            # Incorrect numbers present:
            if check[2] > 0:
                player_score += ((check[1] * 4) + check[0]) - check[2]
            # No incorrect numbers present:
            else:
                player_score += ((check[1] * 4) + check[0])
            print(Fore.GREEN + f'You have guessed {check[0]} correct numbers and {check[1]} correct positions. STATEMENT 2' + Fore.RESET)
            print(Fore.GREEN + f'Your score increased! Your score: {player_score}' + Fore.RESET)
        
        # Print the user's past guesses and number of remaining guesses:
        print(Fore.YELLOW + f'You have {remaining_guesses} remaining guesses.' + Fore.YELLOW)
        print(Fore.YELLOW + f'Your past guesses: {guesses} \n' + Fore.RESET)

    # Winning logic:
    if mastermind.combination_found:
        print(Fore.GREEN + 'Congratulations! You have guessed the hidden combination correctly.' + Fore.RESET)
    else:
        print(Fore.RED +'You failed to guess the combination.')

def hint():
    print('HINT!')

if __name__ == '__main__':
    main()