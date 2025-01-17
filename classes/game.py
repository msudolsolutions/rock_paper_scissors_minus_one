from classes.shapes import Rock, Paper, Scissors, Shape
import random
import re


# Game Class
class RockPaperScissorsMinusOneGame:
    def __init__(self):
        self.shapes = {"rock": Rock(), "paper": Paper(), "scissors": Scissors()}
        self.computer_shapes = []

    def get_shape(self, shape_name: str) -> Shape:
        return self.shapes[shape_name.lower()]

    def get_computer_shapes(self) -> list:
        self.computer_shapes = random.choice(list(self.shapes.values())), random.choice(list(self.shapes.values()))
        return self.computer_shapes

    def get_final_computer_shape(self) -> Shape:
        return random.choice(self.computer_shapes)

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
            return "You win!"
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
