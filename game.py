def rpc_game():
    while True:
        Player1 = input("Player 1 choose (rock, paper, scissors): ")
        actions = ["rock", "paper", "scissors"]
        Player2 = input("Player 2 choose (rock, paper, scissors): ")
        print(f"Player 1 {Player1}, Player 2 {Player2}.")

        if Player1 == Player2:
            print("It's a tie!")
        elif Player1 == "rock":
            if Player2 == "scissors":
                print("You win!")
            else:
                print("You lose.")
        elif Player1 == "paper":
            if Player2 == "rock":
                print("You win!")
            else:
                print("You lose.")
        elif Player1 == "scissors":
            if Player2 == "paper":
                print("You win!")
            else:
                print("You lose.")

        play_again = input("Play again? (yes/no): ")
        if play_again != "yes":
            break



rpc_game()