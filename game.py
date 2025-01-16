import random
from abc import ABC, abstractmethod


# Strategy Interface
class Shape(ABC):
    @abstractmethod
    def beats(self, other: "Shape") -> bool:
        pass

    @abstractmethod
    def name(self) -> str:
        pass


# Concrete Strategies
class Rock(Shape):
    def beats(self, other: "Shape") -> bool:
        return isinstance(other, Scissors)

    def name(self) -> str:
        return "Rock"


class Paper(Shape):
    def beats(self, other: "Shape") -> bool:
        return isinstance(other, Rock)

    def name(self) -> str:
        return "Paper"


class Scissors(Shape):
    def beats(self, other: "Shape") -> bool:
        return isinstance(other, Paper)

    def name(self) -> str:
        return "Scissors"


# Game Class
class RockPaperScissorsGame:
    def __init__(self):
        self.shapes = {"rock": Rock(), "paper": Paper(), "scissors": Scissors()}

    def get_computer_shape(self) -> Shape:
        return random.choice(list(self.shapes.values()))

    def get_player_shape(self, player_input: str) -> Shape:
        return self.shapes[player_input.lower()]

    def play_round(self, player_shape: Shape, computer_shape: Shape):
        if player_shape.beats(computer_shape):
            return "Player wins!"
        elif computer_shape.beats(player_shape):
            return "Computer wins!"
        else:
            return "It's a tie!"


# Main Script
def main():
    game = RockPaperScissorsGame()
    print("Welcome to Rock, Paper, Scissors!")
    print("Type 'rock', 'paper', or 'scissors' to play, or 'quit' to exit.")

    while True:
        player_input = input("\nYour move: ").strip().lower()
        if player_input == "quit":
            print("Thanks for playing!")
            break

        if player_input not in game.shapes:
            print("Invalid shape! Please try again.")
            continue

        player_shape = game.get_player_shape(player_input)
        computer_shape = game.get_computer_shape()

        print(f"\nYou chose {player_shape.name()}.")
        print(f"Computer chose {computer_shape.name()}.")
        result = game.play_round(player_shape, computer_shape)
        print(result)


if __name__ == "__main__":
    main()
