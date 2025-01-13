import os
from time import sleep
from typing import Union, Any

def clear_terminal() -> Union[Any, None]:
    return os.system('cls' if os.name == 'nt' else 'clear')


def display_opt():
    try:
        options = ["Add", "Remove", "Show", "Exit"]
        print("__Option__:")

        for idx, opt in enumerate(options, start=1):
            print(f"[{idx}].{opt}")

        action: int = int(input("Enter Number: "))

        if len(options)< action < 0:
            raise IndexError("Illegal input")
        else:
            return options[action-1]

    except IndexError as error:
        print(f"Error 404 - Not Found: {error}")
        return None


def add_item(tasks) -> list:
    def set_priority() -> str:
        levels = ["emergency_pos","high", "medium", "low"]

        for idx,level in enumerate(levels,start=1):
            print(f"[{idx}]. {level}")

        priority = input("Enter Priority [Number/Description]: ")

        if isinstance(priority,str) and priority.lower() in levels:
            return priority
        elif isinstance(priority,int) and priority in range(1,len(levels)):
            return levels[priority-1]


    def inserting_task(tasks,task,importance) -> list:
        found = False
        def override(lst,act,pos) -> Union[list,None]:
            check = input("Would you like to Override this task? [y/n]: ").lower()
            if check[0] not in ["y","n"] or check[0] == 'y':
                lst.insert(pos,act)
            return lst

        pos = 0

        if importance == "emergency_pos":
            if tasks[0] != " ":
                print("Emergency Slot Taken")
                pos = 0
        else:

            if importance == "high":
                position = [i for i in range(1, 4)]
            elif importance == "medium":
                position = [i for i in range(1, 4)]
            else:
                position = [i for i in range(7, 11)]

            for i in position:
                if i == " ":
                    found = True
                    pos = position.index(i)
                    break

        if found:
            tasks = override(tasks, task, pos)
        return tasks

    try:
        if len(tasks)>10:
            raise IndexError

        task = input("Enter Task: ")
        priority = set_priority()
        tasks = inserting_task(tasks,task,priority)
        return tasks
    except IndexError:
        print("Tasks full - Complete a few tasks")
        return tasks


def remove_item(tasks) -> list:
    pass


def show_item(tasks):
    lst = {
        "emergency": [],
        "high": [],
        "medium": [],
        "low":[]
    }

    for i in range(len(tasks)):
        if i == 0:
            lst["emergency"].append(tasks[i])
        elif i in range(1,4):
            lst["high"].append(tasks[i])
        elif i in range(4,7):
            lst["medium"].append(tasks[i])
        else:
            lst["low"].append(tasks[i])

    for key,values in lst.items():
        print(f"{key.capitalize()}:")
        for num,value in enumerate(values,start=1):
            print(f"\t[{num}].{value}")
        print()


def main():
    tasks = [" " for _ in range(10)]
    clear_terminal()
    print("__Task Manager__")

    try:
        while True:
            option = display_opt()

            if option == "Add":
                tasks = add_item(tasks)
                print("__Task Successfully Added")
                sleep(0.5)
                clear_terminal()
            elif option == "Remove":
                tasks = remove_item(tasks)
                print("__Task Successfully Removed")
                sleep(0.5)
                clear_terminal()
            elif option == "Show":
                clear_terminal()
                show_item(tasks)
            else:
                raise SystemExit

    except (KeyboardInterrupt, SystemExit):
        print("\nExiting...")



if __name__ == '__main__':
    main()