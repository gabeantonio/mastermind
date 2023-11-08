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

        mastermind = Mastermind('1234')
        while mastermind.continue_guessing:
            user_guess = input('Type your guess here: ')
            
            mastermind.add_guess(user_guess)
            guesses = mastermind.view_guesses()
            print('GUESSES --> ', guesses)

            if mastermind.combination_found():
                print('Congratulations! You have guessed the hidden combination correctly!')
                break
            else:
                print('Try again!')

    if __name__ == '__main__':
        main()