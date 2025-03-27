"""
The Library file of the game
"""


import dataclasses
import enum
import typing


class Goal(enum.IntEnum):
    """The goal of the stage"""
    MORE = 1
    LESS = 2
    ODD = 3
    EVEN = 4
    BORDER = 5
    FIX = 6
    CLING = 7
    YOU = 8


@dataclasses.dataclass
class Pos:
    """
    A position on the grid
    Attributes:
        w (int): the column
        h (int): the row
    """
    w: int = 0
    h: int = 0

    def __str__(self) -> str:
        return f"({self.w}, {self.h})"


Coord = int | Pos


class Grid:
    """
    The grid of the game

    Attributes:
        __width (const private int): the width of the grid
        __height (const private int): the height of the grid
        __data (private list[bool]): grid but linear

    You can not get or set attributes\n
    But you can get or set items (ex: `grid = Grid(w, h)`):
    - `grid[Pos(x, y)]` is like `grid.__data[x + y * grid.__width]`
    - `grid[x]` is like `grid.__data[x]`
    """
    def __init__(self: "Grid", width: int, height: int, grid: list[bool]) -> None:
        self.__width = width
        self.__height = height
        self.__data = grid.copy()

    def __getitem__(self: "Grid", key: typing.Any) -> bool:
        if not isinstance(key, Coord):
            raise TypeError("Index must be an int or a Pos")

        pos: int = -1
        if isinstance(key, Pos):
            pos = key.w + key.h * self.__width
        else:
            pos = key

        if pos < 0 or pos >= (self.__width * self.__height):
            raise IndexError("Index out of range")
        return self.__data[pos]

    def __setitem__(self: "Grid", key: typing.Any, value: typing.Any) -> None:
        if not isinstance(key, Coord):
            raise TypeError("Index must be an int or a Pos")
        if not isinstance(value, bool):
            raise TypeError("Value must be a boolean")

        pos: int = -1
        if isinstance(key, Pos):
            pos = key.w + key.h * self.__width
        else:
            pos = key

        if pos < 0 or pos >= (self.__width * self.__height):
            raise IndexError("Index out of range")
        self.__data[pos] = value

    def __len__(self: "Grid") -> int:
        return len(self.__data)

    def __contains__(self: "Grid", item: bool) -> bool:
        return item in self.__data

    def __iter__(self: "Grid"):
        return iter(self.__data)

    def __next__(self: "Grid") -> bool:
        return next(self.__iter__())


class StageData:
    """
    The class for the stage data

    Attributes:
        WIDTH (const int): the width of the grid
        HEIGHT (const int): the height of the grid
        GOAL (const Goal): the goal of the stage
        LAST_GEN (const int): the last generation
        grid (Grid): the grid of the stage
        moves (int): the number of moves
        gen (int): the current generation

    You can not set attributes
    """
    def __init__(self: "StageData", width: int, height: int, goal: int, last_gen: int, grid: list[bool]) -> None:
        self.WIDTH: int = width
        self.HEIGHT: int = height
        self.GOAL: Goal = Goal(goal)
        self.LAST_GEN: int = last_gen
        self.grid: Grid = Grid(width, height, grid)
        self.moves: int = 0
        self.gen: int = 0
