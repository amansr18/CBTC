def get_secret_number():
    while True:
        secret_number = input("Enter a multi-digit secret number (no spaces or letters): ")
        if secret_number.isdigit():
            return secret_number
        else:
            print("Invalid input. Please enter a valid multi-digit number.")

def get_guess(number_length):
    while True:
        guess = input(f"Enter your guess ({number_length} digits): ")
        if guess.isdigit() and len(guess) == number_length:
            return guess
        else:
            print(f"Invalid input. Please enter a {number_length}-digit number.")

def provide_feedback(secret, guess):
    correct_digits = sum(1 for s, g in zip(secret, guess) if s == g)
    return correct_digits

def play_game(player_number):
    print(f"Player {player_number}, set your secret number.")
    secret_number = get_secret_number()
    attempts = 0
    
    while True:
        print(f"Player {3 - player_number}, it's your turn to guess.")
        guess = get_guess(len(secret_number))
        attempts += 1
        if guess == secret_number:
            print(f"Congratulations Player {3 - player_number}! You guessed the number in {attempts} attempts.")
            return attempts
        else:
            correct_digits = provide_feedback(secret_number, guess)
            print(f"Correct digits in the correct place: {correct_digits}")

def main():
    print("Welcome to the Mastermind Game!")
    
    print("Player 1's turn:")
    attempts_player1 = play_game(player_number=1)
    
    print("\nPlayer 2's turn:")
    attempts_player2 = play_game(player_number=2)
    
    if attempts_player1 < attempts_player2:
        print("Player 1 wins and is crowned Mastermind!")
    elif attempts_player2 < attempts_player1:
        print("Player 2 wins and is crowned Mastermind!")
    else:
        print("It's a tie! Both players are equally good at this game.")
        
if __name__ == "__main__":
    main()
