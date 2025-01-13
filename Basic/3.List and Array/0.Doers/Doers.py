import os
import random
from typing import Union, Any


def clear_terminal() -> Union[Any, None]:
    return os.system('cls' if os.name == 'nt' else 'clear')


def display_opt():
    try:
        options = ["Add", "Remove", "Show", "Exit"]
        print("__Option__:")

        for idx, opt in enumerate(options, start=1):
            print(f"{idx}. {opt}")

        action: int = int(input("Enter Number: "))

        if len(options)< action < 0:
            raise IndexError("Illegal input")
        else:
            return options[action-1]

    except IndexError as error:
        print(f"Error 404 - Not Found: {error}")
        return None


def add_item(tasks) -> list:
    def set_priority(task) -> str:
        levels = ["emergency_pos","high", "medium", "low"]

        for idx,level in enumerate(levels,start=1):
            print(f"[{idx}]. {level}")

        priority = input("Enter Priority [Number/Description]: ")

        if isinstance(priority,str) and priority.lower() in levels:
            return priority
        elif isinstance(priority,int) and priority in range(1,len(levels)):
            return levels[priority-1]


    def inserting_task(tasks,task,importance) -> list:
        def override(lst,act,pos) -> list:
            check = input("Would you like to Override this task? [y/n]: ").lower()
            if check[0] not in ["y","n"] or check[0] == 'y':
                lst.insert(pos,act)
            return lst

        position = 0

        if importance == "emergency_pos":
            if tasks[0] != " ":
                print("Emergency Slot Taken")
                position = 0
        else:
            if importance == "high":
                position = [i for i in range(1, 4)]
            elif importance == "medium":
                position = [i for i in range(1, 4)]
            else:
                position = [i for i in range(7, 11)]




        tasks = override(tasks, task, position)
        return tasks

    try:
        if len(tasks)>10:
            raise IndexError

        task = input("Enter Task: ")
        priority = set_priority(task)
        tasks = inserting_task(tasks,task,priority)

        return tasks
    except IndexError:
        print("Tasks full - Complete a few tasks")
        return tasks


def remove_item(tasks) -> list:
    pass


def show_item(tasks):
    pass


def main():
    tasks = [" " for _ in range(10)]
    print(tasks)
    clear_terminal()
    print("__Task Manager__")

    try:
        while True:
            option = display_opt()

            if option == "Add":
                tasks = add_item(tasks)
            elif option == "Remove":
                tasks = remove_item(tasks)
            elif option == "Show":
                show_item(tasks)
            else:
                raise SystemExit

    except (KeyboardInterrupt, SystemExit):
        print("\nExiting...")



if __name__ == '__main__':
    main()