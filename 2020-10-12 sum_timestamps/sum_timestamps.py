from typing import List


def sum_timestamps(ts_str: List[str]) -> str:
    total_seconds = sum( # total seconds in all timestamps
        sum( # seconds in one timestamp
            int(hms) * mult
            for hms, mult # quantity of time and multiplier
            in zip( # only loops as many items as are in timestamp
                reversed(t_str.split(":")), # get seconds, minutes, hours (optional)
                (1, 60, 3600) # multipliers to convert hms to seconds
            )
        )
        for t_str in ts_str
    )

    hours, r = divmod(total_seconds, 3600)
    minutes, seconds = divmod(r, 60)
    
    if hours:
        return f"{hours}:{minutes:02d}:{seconds:02d}"
    else:
        return f"{minutes}:{seconds:02d}"
