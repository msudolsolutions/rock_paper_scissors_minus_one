from classes.game import RockPaperScissorsMinusOneGame


# Main Script
def main():
    game = RockPaperScissorsMinusOneGame()
    print("\nWelcome to Rock, Paper, Scissors minus One!\n\n"
          "How to play: (Write 'quit' anytime to exit the game)\n"
          "1. Choose two shapes from 'rock', 'paper' and 'scissors'.\n"
          "2. The computer will also choose two shapes.\n"
          "3. Both yours and computer's shapes are revealed.\n"
          "4. Choose the shape that you think will win.\n"
          "5. The computer also chooses one of the shapes.\n"
          "6. The chosen shapes are compared and the winner is determined.")

    while True:
        player_input = input("\nYour shapes: ").strip().lower()
        if player_input == "quit":
            print("Thanks for playing!")
            break
        player_shapes = game.get_player_shapes(player_input)
        computer_shapes = game.get_computer_shapes()
        print(f"The computer's shapes: {computer_shapes[0].name()}, {computer_shapes[1].name()}")

        player_shape = input("\nWhat shape do you want to leave: ").strip().lower()
        if player_shape == "quit":
            print("Thanks for playing!")
            break
        elif (game.get_shape(player_shape) not in player_shapes):
            print("Invalid shape. Please choose one of the shapes you have.")
            continue
        else:
            player_shape = game.get_shape(player_shape)
            computer_shape = game.get_final_computer_shape()

        print(f"\nYou chose {player_shape.name()}.")
        print(f"Computer chose {computer_shape.name()}.")
        result = game.play_round(player_shape, computer_shape)
        print(result)


if __name__ == "__main__":
    main()
