from math import ceil


class float_range:
    def __init__(self, start: float, stop: float = None, step: float = None):
        self.start, self.stop = (0, start) if stop is None else (start, stop)
        self.step = 1 if step is None else step
    
    def __len__(self):
        return max(0, ceil((self.stop - self.start) / self.step))

    def __eq__(self, other):
        def get_id(obj):
            if len(obj):
                return (next(iter(obj)), next(reversed(obj)), len(obj))
            else:
                return ()
        
        try:
            return get_id(self) == get_id(other)
        except:
            return NotImplemented
        
    def __iter__(self):
        val = self.start

        for _ in range(len(self)):
            yield val
            
            val += self.step

    def __reversed__(self):
        val = self.start + (len(self) - 1) * self.step

        for _ in range(len(self)):
            yield val

            val -= self.step
