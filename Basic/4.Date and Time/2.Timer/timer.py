import os
from datetime import time
from typing import Union

def clear_terminal():
    return os.system('cls' if os.name == 'nt' else 'clear')


def custom_timer() -> Union[None,time]:
    try:
        print("\n__Custom Timer__")
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


def display_timer(current_time):
    pass


def option():
    try:
        options = ["Stop","Restart"]

        for key,opt in enumerate(options,start=1):
            print(f"{key}. {opt}")

        selected = int(input(f"Select an option [1-{len(options)}]: "))

        if selected not in range(1,len(options)):
            raise ValueError(f"Illegal Selection")
        else:
            return options[selected-1]

    except ValueError as error:
        print(f"Error 404 - Not found. {error}")
        return None


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
    try:
        decrease_by = time(0,0,1)
        print("__Timer__\n")
        end_time = time(0,0,0)
        opt = retrieve_start_time()

        if opt == "Custom":
            start_time = custom_timer()
        else:
            hour, minute, second = opt.split(":")
            start_time = time(int(hour), int(minute), int(second))

        if start_time is None:
            raise ValueError(f"Start time can't be None")
        else:
            print(f"Starting Timer at {start_time}")

            while start_time < end_time:
                current_time = start_time - decrease_by
                opt = option()



    except ValueError as error:
        print(f"{error}")



if __name__ == '__main__':
    main()