from collections import deque
from itertools import islice
from typing import Iterable


def window(it: Iterable, n: int):
    if n > 0:
        it = iter(it)

        last_n = deque(islice(it, n - 1), maxlen=n)

        for val in it:
            last_n.append(val)

            yield tuple(last_n)
