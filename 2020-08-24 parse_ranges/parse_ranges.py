
def parse_ranges(ranges_str: str):
    """Convert a string representing a comma separated list of hypen separated ranges into an iterator that returns the ints in those ranges"""
    
    valid_ranges = []
    for range_str in ranges_str.split(","):
        stripped_range_str = range_str.strip()

        if "->" in stripped_range_str: # ignore arrow and subsequent chars
            arrow_i = stripped_range_str.index("->")
            valid_ranges.append([int(stripped_range_str[:arrow_i])])
        elif all(map(str.isdigit, stripped_range_str)): # single number
            valid_ranges.append([int(stripped_range_str)])
        elif all(c == "-" or c.isdigit() for c in stripped_range_str): # normal range
            start, _, end = range_str.partition("-")
            valid_ranges.append([int(start), int(end) + 1])

    for valid_range in valid_ranges:
        if len(valid_range) == 1:
            yield valid_range[0]
        else:
            yield from range(*valid_range)
