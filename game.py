from abc import ABC, abstractmethod
import random
import re


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
class RockPaperScissorsMinusOneGame:
    def __init__(self):
        self.shapes = {"rock": Rock(), "paper": Paper(), "scissors": Scissors()}

    def get_shape(self, shape_name: str) -> Shape:
        return self.shapes[shape_name.lower()]

    def get_computer_shapes(self) -> list:
        return random.choice(list(self.shapes.values())), random.choice(list(self.shapes.values()))

    def get_player_shapes(self, player_input: str) -> list:
        player_shapes = self.__parse_moves(player_input)
        if len(player_shapes) != 2:
            raise Exception("Invalid input! Please provide exactly two moves (e.g., 'rock, paper').")
        player_shape1, player_shape2 = player_shapes
        if (self.__validate_shape(player_shape1) is False or self.__validate_shape(player_shape2) is False):
            raise Exception("Invalid moves! Use 'rock', 'paper', or 'scissors'.")
        return self.get_shape(player_shape1), self.get_shape(player_shape2)

    def play_round(self, player_shape: Shape, computer_shape: Shape):
        if player_shape.beats(computer_shape):
            return "Player wins!"
        elif computer_shape.beats(player_shape):
            return "Computer wins!"
        else:
            return "It's a tie!"
    
    def __validate_shape(self, shape: str) -> bool:
        if shape.lower() not in self.shapes:
            return False
        return True

    @staticmethod
    def __parse_moves(user_input: str):
        moves = re.split(r"\s*,\s*|\s+and\s+|\s+", user_input.strip(), maxsplit=2)
        return moves


# Main Script
def main():
    game = RockPaperScissorsMinusOneGame()
    print("Welcome to Rock, Paper, Scissors minus One!\n"
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

        player_shape = input("\nWhat shape you want to leave: ").strip().lower()
        if player_input == "quit":
            print("Thanks for playing!")
            break
        elif (game.get_shape(player_shape) not in player_shapes):
            print("Invalid shape. Please choose one of the shapes you have.")
            continue
        else:
            player_shape = game.get_shape(player_shape)
            computer_shape = random.choice(computer_shapes)

        print(f"\nYou chose {player_shape.name()}.")
        print(f"Computer chose {computer_shape.name()}.")
        result = game.play_round(player_shape, computer_shape)
        print(result)


if __name__ == "__main__":
    main()
