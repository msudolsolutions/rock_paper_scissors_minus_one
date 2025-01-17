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
