from typing import Iterable


def uniques_only(iterator: Iterable) -> Iterable:
    yielded = set()

    for item in iterator:
        try:
            # "not in" fails if item is unhashable
            if item not in yielded:
                yielded.add(item)

                yield item
        except TypeError:
            # strings are hashable
            str_item = str(item)

            if str_item not in yielded:
                yielded.add(str_item)

                yield item
