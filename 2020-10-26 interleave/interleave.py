from typing import Iterable


def interleave(it1: Iterable, it2: Iterable):
    for a, b in zip(it1, it2):
        yield a
        yield b
