from datetime import date
from calendar import monthrange


class Month:
    # suppresses creation of __dict__
    __slots__ = "year", "month"

    def __init__(self, year: int, month: int):
        # immutable so need to use super's __setattr__
        super().__setattr__("year", year)
        super().__setattr__("month", month)

    # make immutable
    def __setattr__(self, name, value):
        raise AttributeError

    def __delattr__(self, name):
        raise AttributeError

    # string representations
    def __repr__(self):
        return f"Month({self.year}, {self.month})"

    def __str__(self):
        return f"{self.year:04d}-{self.month:02d}"

    # make hashable
    def __hash__(self):
        return 100 * self.year + self.month
    
    # comparisons
    def __eq__(self, other):
        if isinstance(other, Month):
            return self.year == other.year and self.month == other.month
        else:
            return False
    
    def __gt__(self, other):
        if isinstance(other, Month):
            return self.month > other.month if self.year == other.year else self.year > other.year
        else:
            raise TypeError

    def __ge__(self, other):
        return self > other or self == other

    def __lt__(self, other):
        return not self >= other

    def __le__(self, other):
        return not self > other

    # factory class methods
    @classmethod
    def from_date(cls, date_: date):
        return cls(date_.year, date_.month)

    # instance methods
    def strftime(self, format: str):
        return date(self.year, self.month, 1).strftime(format)

    # properties
    @property
    def first_day(self):
        return date(self.year, self.month, 1)

    @property
    def last_day(self):
        _, num_days = monthrange(self.year, self.month)

        return date(self.year, self.month, num_days)
