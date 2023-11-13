from mastermind import Mastermind
import requests
from colorama import Fore

def main():
    hidden_combination = get_random_combination()
    player_score = 0
    play_game(hidden_combination, player_score)

def play_game(hidden_combination: str, player_score: int):
    mastermind = Mastermind(hidden_combination)
    while mastermind.continue_guessing():
        user_guess = input('Type your guess here: ')
        if len(user_guess) < mastermind.COMBO_LENGTH:
            print(Fore.RED + f'Input too short. Please make sure your input is {mastermind.COMBO_LENGTH} digits long. \n' + Fore.RESET)
            continue
        elif len(user_guess) > mastermind.COMBO_LENGTH:
            print(Fore.RED + f'Input too long. Please make sure your input is only {mastermind.COMBO_LENGTH} long. \n' + Fore.RESET)
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
        display_guesses(correct_numbers, correct_positions, player_score, remaining_guesses, guesses)
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