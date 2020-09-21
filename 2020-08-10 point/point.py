# python 3.8

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float
    z: float

    def __eq__(self, other):
        return all(
            getattr(self, axis) == getattr(other, axis)
            for axis
            in ("x", "y", "z")
        )

    def __add__(self, other):
        return Point(
            x=(self.x + other.x),
            y=(self.y + other.y),
            z=(self.z + other.z)
        )

    def __sub__(self, other):
        return Point(
            x=(self.x - other.x),
            y=(self.y - other.y),
            z=(self.z - other.z)
        )
    
    def __mul__(self, other):
        if isinstance(other, (float, int)):
            return Point(
                x=(self.x * other),
                y=(self.y * other),
                z=(self.z * other)
            )
        else:
            raise TypeError("Can only multiply by a number")
    
    # __iter__ allows multiple assigment using the * operator
    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z
