from aoc_lib.basic.regex import find_all_integers


class Coord2D():
    def __init__(self, data: tuple[int, int] | list[int] | str):
        self.x, self.y = Coord2D.get(data)

    def __repr__(self):
        return f"({self.x},{self.y})"

    @property
    def row(self):
        return self.x

    @property
    def col(self):
        return self.y

    @property
    def as_list(self):
        return [self.x, self.y]

    @property
    def as_tuple(self):
        return (self.x, self.y)

    def get(data: tuple[int, int] | list[int] | str) -> tuple[int, int]:
        if type(data) == tuple:
            return data
        elif type(data) == list:
            return tuple(data)
        elif type(data) == str:
            return tuple(find_all_integers(data))
        else:
            raise NotImplementedError

    def max(tuples: list[tuple[int]]):
        return max(x for x, _ in tuples), max(y for _, y in tuples)
