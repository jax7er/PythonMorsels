
class float_range:
    def __init__(self, end_start: float, end: float = None, step: float = None):
        self.start = float(0 if end is None else end_start)
        self.end = float(end_start if end is None else end)
        self.step = float(1 if step is None else step)

        self._value = self.start

        if self._values_remaining():
            while self._values_remaining():
                self._value += self.step
            
            self._last = self._value - self.step
            self._value = self.start
        else:
            self._last = self.end
    
    def __len__(self):
        self._value = self._last

        if self._values_remaining():
            return 1 + int((self._last - self.start) // self.step)
        else:
            return 0

    def __eq__(self, other):
        try:
            if len(other) != len(self):
                return False
        except TypeError: # other has no __len__
            pass

        try:
            it_self = iter(self)
            it_other = iter(other)

            if not all(x == y for x, y in zip(it_self, it_other)):
                return False
        except TypeError: # other is not iterable
            return False

        try:
            next(it_self)
            return False
        except StopIteration: # this iterable is exhausted
            pass
        
        try:
            next(it_other)
            return False
        except StopIteration: # other iterable is exhausted
            pass

        return True

    def __iter__(self):
        self._value = self.start

        while self._values_remaining():
            yield self._value

            self._value += self.step

    def __reversed__(self):
        self._value = self._last

        while self._values_remaining():
            yield self._value

            self._value -= self.step
    
    def _values_remaining(self):
        if self.step >= 0:
            return self.start <= self._value < self.end
        else:
            return self.start >= self._value > self.end

x = float_range(1, 100, 1.1)
y = float_range(1, 99, 1.1)
print(len(x), len(y))
print(list(x)[:5], list(y)[:5])
print(list(reversed(x))[:5], list(reversed(y))[:5])
print(x == y)
print(x == range(1, 99))
print(y == range(1, 99))
