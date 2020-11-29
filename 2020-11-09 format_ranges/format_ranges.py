from statistics import mean
from typing import Iterable


def format_ranges(numbers: Iterable):
    nums = list(sorted(numbers))  # sort the numbers

    ranges = []

    while nums:
        # pop the smallest number in the list
        start = end = nums.pop(nums.index(min(nums)))

        # keep popping elements while they are in the range
        while (end + 1) in nums:
            end = nums.pop(nums.index(end + 1))

        # append a set to remove duplicate start/end
        ranges.append({start, end})
    
    # use mean of ranges to sort
    ranges.sort(key=mean)

    # format numbers/ranges
    return ",".join("-".join(map(str, sorted(r))) for r in ranges)
