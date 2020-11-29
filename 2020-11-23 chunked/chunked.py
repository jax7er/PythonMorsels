from itertools import zip_longest
from typing import Iterable

SENTINEL = object()


def chunked(iterable: Iterable, n: int, *, fill = SENTINEL):
    iter_copies = [iter(iterable)] * n

    chunks = zip_longest(*iter_copies, fillvalue=fill)

    for chunk in chunks:
        yield [x for x in chunk if x is not SENTINEL]
