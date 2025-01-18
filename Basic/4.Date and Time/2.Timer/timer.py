from datetime import time


def custom_timer():
    pass


def display_timer():
    pass


def retrieve_start_time():
    default_times = ["00:45:00", "00:30:00", "00:15:00", "00:10:00", "00:05:00", "00:00:30", "Custom"]
    try:
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
    end_time = time(0,0,0)
    opt = retrieve_start_time()

    if opt == "Custom":
        start_time = custom_timer()
    else:
        hour, minute, second = opt.split(":")
        start_time = time(int(hour), int(minute), int(second))


if __name__ == '__main__':
    main()