from mastermind import Mastermind
import requests
from colorama import Fore
import math
import time

def main():
    intro()
    difficulty = input(Fore.RED + 'Do you want to play on a hard difficulty level? Type Yes or No: ' + Fore.RESET)
    if difficulty.lower() == 'yes':
        hidden_combination = get_random_combination(5)
    else:
        hidden_combination = get_random_combination(4)
    player_score = 0
    play_game(hidden_combination, player_score)

def play_game(hidden_combination: str, player_score: int):
    mastermind = Mastermind(hidden_combination)
    start = time.time()
    while mastermind.continue_guessing():
        user_guess = input('Type your guess here: ')
        if not user_guess.isnumeric():
            print(Fore.RED + f'Please enter numbers only. \n' + Fore.RESET)
            continue
        if len(user_guess) < len(hidden_combination):
            print(Fore.RED + f'Input too short. Please make sure your input is {len(hidden_combination)} digits long. \n' + Fore.RESET)
            continue
        elif len(user_guess) > len(hidden_combination):
            print(Fore.RED + f'Input too long. Please make sure your input is only {len(hidden_combination)} long. \n' + Fore.RESET)
            continue
        mastermind.add_guess(user_guess)
        result = mastermind.check_guess(user_guess)
        correct_numbers, correct_positions, correct_instances = result[0], result[1], result[2]
        guesses = mastermind.view_guesses()
        remaining_guesses = mastermind.remaining_guesses()
        if correct_numbers == 0:
            hint_needed = input(Fore.RED + f'Sorry, those are all incorrect. Do you need a hint? Type Yes or No: ' + Fore.RESET)
            mastermind.hint(hint_needed)
        if correct_positions == 0:
            player_score += correct_instances
        else:
            player_score += (correct_positions * 4) + correct_instances
        display_stats(correct_numbers, correct_positions, player_score, remaining_guesses, guesses)
    if mastermind.combination_found:
        end = time.time()
        print(Fore.GREEN + f'Congratulations! You have guessed the hidden combination correctly. You guessed it in {math.floor(end - start)} seconds. Can you guess it faster next time?' + Fore.RESET)
    else:
        print(Fore.RED + f'You failed to guess the combination. The hidden combination was: {hidden_combination}')

def get_random_combination(difficulty: int):
    api_url = f"https://www.random.org/integers/?num={difficulty}&min=0&max=7&col=1&base=10&format=plain&rnd=new"
    response = requests.get(api_url)
    if response.status_code == 200:
        hidden_combination = f'{response.text}'.replace('\n', '')
        return hidden_combination
    else:
        print(f'Failed to get a random combination. Status code: {response.status_code}')

def display_stats(correct_numbers: int, correct_positions: int, player_score: int, remaining_guesses: int, guesses: list):
    print(Fore.GREEN + f'You have guessed {correct_numbers} correct numbers and {correct_positions} correct positions.' + Fore.RESET)
    print(Fore.GREEN + f'Your score: {player_score}' + Fore.RESET)
    print(Fore.YELLOW + f'You have {remaining_guesses} remaining guesses.' + Fore.YELLOW)
    print(Fore.YELLOW + f'Your past guesses: {guesses} \n' + Fore.RESET)

def intro():
    print('Welcome to Mastermind!\nAt the start of the game, the computer will randomly select a pattern of 4 or 5 different numbers\n(depending on the difficulty you choose) from a total of 8 different numbers.\nYou will have 10 attempts to guess the number combinations.\nAfter each attempt, the computer will provide you some feedback regarding your most recent guess.\nGood luck! \n')

if __name__ == '__main__':
    main()