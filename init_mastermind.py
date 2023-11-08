from mastermind import Mastermind
import requests

class Play:
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

        mastermind = Mastermind(hidden_combination)
        while mastermind.continue_guessing:
            user_guess = input('Type your guess here: ')
            # Input validation:
            if len(user_guess) < mastermind.COMBO_LENGTH:
                print(f'Input too short. Please make sure your input is {mastermind.COMBO_LENGTH} digits long. \n')
                continue
            elif len(user_guess) > mastermind.COMBO_LENGTH:
                print(f'Input too long. Please make sure your input is only {mastermind.COMBO_LENGTH} long. \n')
                continue
            
            mastermind.add_guess(user_guess)
            check = mastermind.check_guess(user_guess)
            guesses = mastermind.view_guesses()
            remaining_guesses = mastermind.remaining_guesses()

            print(f'You have guessed {check[0]} correct numbers and {check[1]} correct positions')
            print(f'You have {remaining_guesses} remaining guesses.')
            print(f'Your past guesses: {guesses}')

            if mastermind.combination_found():
                print('Congratulations! You have guessed the hidden combination correctly!')
                break
            else:
                print('Try again! \n')

    if __name__ == '__main__':
        main()