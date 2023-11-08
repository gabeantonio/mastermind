from mastermind import Mastermind

class Play:
    def main():
        print('Hello World!')
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