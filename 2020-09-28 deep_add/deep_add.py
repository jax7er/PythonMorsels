
def deep_add(arg, start = None):
    total = start

    try: # check iterable
        list_arg = list(arg)
    except TypeError: # not iterable
        if arg is None: # check None
            raise
        else: # summable type
            total = total + value if total else value
    else: # iterable
        for value in list_arg:
            try: # check iterable
                list_value = list(value)
            except TypeError: # not iterable
                total = total + value if total else value
            else: # iterable
                if list_value: # check not empty
                    # recursion
                    value = deep_add(list_value, 0)

                    total = total + value if total else value
    
    return total or 0
