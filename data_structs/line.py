from aoc_lib.basic.regex import find_all_integers
from aoc_lib.data_structs.coord import Coord2D


class Line():
    def __init__(self, string: str, spacer=None):
        self.start, self.end = self._get_coordinates(string, spacer)
        self.min_x, self.max_x = sorted([self.start.x, self.end.x])
        self.min_y, self.max_y = sorted([self.start.y, self.end.y])

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return f"Line: {self.start} -> {self.end}"

    def _get_coordinates(self, string: str, spacer: str | None):
        if spacer:
            string = string.replace(spacer, " ")
        numbers = find_all_integers(string)
        return Coord2D(numbers[0:2]), Coord2D(numbers[2:])

    def is_horizontal(self):
        return self.start.x != self.end.x and self.start.y == self.end.y

    def is_vertical(self):
        return self.start.x == self.end.x and self.start.y != self.end.y

    def is_diagonal(self):
        return self.start.x != self.end.x and self.start.y != self.end.y

    def list_points(self):
        if self.is_horizontal():
            return [(x, self.start.y) for x in range(self.min_x, self.max_x + 1)]
        if self.is_vertical():
            return [(self.start.x, y) for y in range(self.min_y, self.max_y + 1)]
        if self.is_diagonal():
            x = [self.start.x, self.end.x]
            y = [self.start.y, self.end.y]
            points = [(x[0], y[0])]
            while min(x) < max(x):
                x[0] = x[0] + 1 if x[0] < x[1] else x[0] - 1
                y[0] = y[0] + 1 if y[0] < y[1] else y[0] - 1
                points.append((x[0], y[0]))
            return points
