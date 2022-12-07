from aoc_lib.basic.regex import find_all_integers


class Coord2D():
    def __init__(self, data: list[int] | str):
        self.x, self.y = Coord2D.get(data)
        self.list = [self.x, self.y]
        self.tuple = (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.x},{self.y})"

    def get(data: list[int] | str) -> tuple[int, int]:
        if type(data) == list:
            return tuple(data)
        elif type(data) == str:
            return tuple(find_all_integers(data))
        else:
            raise NotImplementedError

    def max(tuples: list[tuple[int]]):
        return max(x for x, _ in tuples), max(y for _, y in tuples)
