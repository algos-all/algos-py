from typing import List

from src.geometry.point2d import Point2D
from src.geometry.point2d import cw


class ConvexHull2D:

    def __init__(self, points: List[Point2D]):

        self.outer = []
        self.upper = []
        self.lower = []

        self.index = 0

        if len(points) == 0:
            return

        self.outer = sorted(points)

        # TODO: could look for a faster solution to remove duplicates
        self.outer = [self.outer[0]] + [
            q for p, q in zip(self.outer, self.outer[1:]) if p != q
        ]

        if len(self.outer) <= 2:
            self.upper = self.outer[:]
            self.lower = self.outer[:]

            return

        self.upper = [self.outer[0], self.outer[1]]
        self.lower = [self.outer[0], self.outer[1]]

        for point in self.outer[2:]:

            while cw(self.upper[-2], self.upper[-1], point) != +1:
                self.upper.pop()

                if len(self.upper) == 1:
                    break

            while cw(self.lower[-2], self.lower[-1], point) != -1:
                self.lower.pop()

                if len(self.lower) == 1:
                    break

            self.upper.append(point)
            self.lower.append(point)

        self.outer = self.upper[:] + self.lower[
            len(self.lower) - 2:0:-1
        ]

    def __len__(self):
        return len(self.outer)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self):
            self.index = 0

            raise StopIteration

        self.index += 1

        return self.points[self.index - 1]

    def __getitem__(self, key):
        return self.outer[key]
