import math


class Circle:
    def __init__(self, radius=1):
        self._radius = float(radius)
        self._diameter = 2 * self._radius
        self._area = math.pi * self._radius ** 2
    
    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius > 0:
            self._radius = float(radius)
            self._diameter = 2 * self._radius
            self._area = math.pi * self._radius ** 2
        else:
            raise ValueError("radius cannot be negative")
    
    @property
    def diameter(self):
        return self._diameter

    @diameter.setter
    def diameter(self, diameter):
        if diameter > 0:
            self._diameter = float(diameter)
            self._radius = self._diameter / 2
            self._area = math.pi * self._radius ** 2
        else:
            raise ValueError("diameter cannot be negative")
    
    @property
    def area(self):
        return self._area

    @area.setter
    def area(self, area):
        raise AttributeError("can't set area")

    def __repr__(self):
        return f"Circle({self._radius:.0f})"


def main():
    c = Circle()
    print(c, c.radius, c.diameter, c.area)

    c = Circle(5)    
    print(c, c.radius, c.diameter, c.area)

    c.radius = 10    
    print(c, c.radius, c.diameter, c.area)

    c.diameter = 10    
    print(c, c.radius, c.diameter, c.area)

    try:
        c.area = 10    
        print(c, c.radius, c.diameter, c.area)
    except AttributeError as e:
        print(e)

    try:
        c.radius = -10    
        print(c, c.radius, c.diameter, c.area)
    except ValueError as e:
        print(e)


if __name__ == "__main__":
    main()
    