import os
from datetime import datetime, timedelta
import time as t
from typing import Union


def clear_terminal():
    """Clears the terminal based on the operating system."""
    return os.system('cls' if os.name == 'nt' else 'clear')


def custom_timer() -> Union[None, timedelta]:
    """Allows the user to set a custom timer."""
    try:
        print("\n__Custom Timer__")
        hours = int(input('Enter Hours: '))
        mins = int(input('Enter Minutes: '))
        secs = int(input('Enter Seconds: '))

        if hours == 0 and mins == 0 and secs == 0:
            raise ValueError("Timer cannot start at 00:00:00.")
        return timedelta(hours=hours, minutes=mins, seconds=secs)

    except (ValueError, TypeError) as error:
        print(f"Error: {error}")
        return None


def display_timer(current_time: timedelta):
    """Displays the current timer countdown."""
    clear_terminal()
    print(f"Time Remaining: {str(current_time)}")


def option() -> Union[str, None]:
    """Allows the user to select an action for the timer."""
    try:
        options = ["Stop", "Restart","Continue"]
        print("\nOptions:")
        for key, opt in enumerate(options, start=1):
            print(f"{key}. {opt}")

        selected = int(input(f"Select an option [1-{len(options)}]: "))

        if selected not in range(1, len(options) + 1):
            raise ValueError("Invalid selection.")
        return options[selected - 1]

    except ValueError as error:
        print(f"Error: {error}")
        return None


def retrieve_start_time() -> Union[timedelta, None]:
    """Retrieves the start time from predefined options or allows custom input."""
    default_times = [
        ("00:45:00", timedelta(minutes=45)),
        ("00:30:00", timedelta(minutes=30)),
        ("00:15:00", timedelta(minutes=15)),
        ("00:10:00", timedelta(minutes=10)),
        ("00:05:00", timedelta(minutes=5)),
        ("00:00:30", timedelta(seconds=30)),
        ("Custom", None)
    ]

    try:
        print("__Time Options__")
        for key, (label, _) in enumerate(default_times, start=1):
            print(f"[{key}]. {label}")

        selected_index = int(input(f"Enter an index [1-{len(default_times)}]: "))
        if not (1 <= selected_index <= len(default_times)):
            raise ValueError("Invalid selection index.")

        label, time_value = default_times[selected_index - 1]
        if label == "Custom":
            return custom_timer()
        return time_value

    except ValueError as error:
        print(f"Error: {error}")
        return None


def main():
    """Main function to execute the timer logic."""
    try:
        print("__Timer__\n")
        decrease_by = timedelta(seconds=1)
        start_time = retrieve_start_time()

        if start_time is None:
            raise ValueError("Failed to set a valid start time.")

        current_time = start_time
        print(f"Starting Timer at {current_time}...")

        while current_time > timedelta(0):
            display_timer(current_time)
            t.sleep(1)
            current_time -= decrease_by

            if current_time <= timedelta(0):
                print("Time's up!")
                break

            opt = option()
            if opt == "Stop":
                print(f"Timer stopped at {current_time}.")
                break
            elif opt == "Restart":
                print(f"Timer restarting at {start_time}.")
                current_time = start_time
            else:
                print(f"Timer at {current_time}.")

    except ValueError as error:
        print(f"Error: {error}")

    except KeyboardInterrupt:
        print("\nTimer interrupted. Goodbye!")


if __name__ == '__main__':
    main()
