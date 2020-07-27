from collections import deque

def tail(it, n):
    return list(deque(it, n)) if n > 0 else []
