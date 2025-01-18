from datetime import time
from typing import Union


def custom_timer() -> Union[None,time]:
    try:
        hours = int(input('Enter Hours: '))
        mins = int(input('Enter Minutes: '))
        secs = int(input('Enter Seconds: '))

        if hours == 0 and mins == 0 and secs == 0:
            timer = time(hours, mins, secs)
            raise ValueError(f"Timer can't start at {timer}")
        else:
            return time(hours, mins, secs)

    except (ValueError, TypeError) as error:
        print(f"Error 404 - Not found. {error}")
        return None


def display_timer():
    pass


def retrieve_start_time():
    default_times = ["00:45:00", "00:30:00", "00:15:00", "00:10:00", "00:05:00", "00:00:30", "Custom"]
    try:
       print("__Time Options__")
       for key,times in default_times:
           print(f"[{key}]. [{times}]")

       selected_time = int(input(f"Enter an index [1-{len(default_times)}]: "))

       if 1 > selected_time > len(default_times):
           raise ValueError(f"Illegal Selection Index {selected_time}")
       return default_times[selected_time-1]

    except ValueError as e:
        print(f"Error 404 - Not Found: {e}")
        return default_times[-1]


def main():
    print("__Timer__\n")
    end_time = time(0,0,0)
    opt = retrieve_start_time()

    if opt == "Custom":
        start_time = custom_timer()
    else:
        hour, minute, second = opt.split(":")
        start_time = time(int(hour), int(minute), int(second))

    if


if __name__ == '__main__':
    main()