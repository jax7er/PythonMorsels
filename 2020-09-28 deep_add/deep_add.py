
def deep_add(arg, start = None):
    total = start

    try:
        list_arg = list(arg)
    except TypeError: # not iterable
        if arg is None:
            raise
        else:
            total = total + value if total else value
    else:
        for value in list_arg:
            try:
                list_value = list(value)
            except TypeError: # not iterable
                total = total + value if total else value
            else:
                if list_value:
                    value = deep_add(list_value, 0)

                    total = total + value if total else value
    
    return total or 0
