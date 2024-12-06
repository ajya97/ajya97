import getpass 

def guesser_game():
    print("Welcome to the Guesser's Game!")
    print("Rules: One player (Chooser) selects a number, and other players (Guessers) try to guess it. ")
    print("Let's get started!\n")

    players = []
    num_players = int(input("Enter the number of players: "))
    for i in range(num_players):
        player_name = input(f"Enter the name of Player {i + 1}: ")
        players.append(player_name)

    print("\nChoose who will be the Chooser.")
    chooser = input("Enter the name of Chooser: ")

    if chooser not in players:
        print("Invalid player name! Restart the game.")
        return
    print(f"\n{chooser}, you will now select a number for others to guess!")
    try:
        secret_number = int(getpass.getpass("Enter the secret number (it will be hidden): "))
    except ValueError:
        print("Invalid input! Please enter a valid number. Restart the game. ")
        return
    

    max_attempts = 2
    attempts = 0
    winners = []

    print("\nGuessers, try to guess the number! You have 2 attempts.\n")
    while attempts < max_attempts:
        guesses = []
        print(f"--- Round {attempts + 1} ---")

        for player in players:
            if player != chooser:
                try:
                    guess = int(input(f"{player}, enter your guess:  "))
                except ValueError:
                    print("Invalid input! Enter a valid number. ")
                    guess = None
                guesses.append((player, guess))

        for player, guess in guesses:
            if guess == secret_number:
                winners.append(player)

        if winners:
            print(f"\nCongratulations! The following players guessed the number {secret_number} correctly: {', '.join(winners)}")
            return
        print("\nNo correct guesses in this round. Moving to the next round. ")
        attempts += 1


    if not winners:
        print(f"\nGame Over one guessed the correct number. The secret number was {secret_number}.")
        print(f"The Chooser, {chooser}, Wins!")
    else:
        print(f"\nCongratulations to the winners: {','.join(winners)}")
    
    print("Thank for playing!")


if __name__ == "__main__":
    guesser_game()


    
