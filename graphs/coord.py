from aoc_lib.basic.regex import find_all_integers


class Coord2D():
    def __init__(self, data: list[int] | str):
        self.x, self.y = self._get_coordinates(data)
        self.list = [self.x, self.y]
        self.tuple = (self.x, self.y)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"({self.x},{self.y})"

    def _get_coordinates(self, data: list[int] | str) -> tuple[int, int]:
        if type(data) == list:
            return tuple(data[0], data[1])
        elif type(data) == str:
            return tuple(find_all_integers(data))
        else:
            raise NotImplementedError

    def max_coords(tuples: list[tuple[int]]):
        return max(x for x, _ in tuples), max(y for _, y in tuples)
