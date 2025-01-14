def search():
    pass


def sort():
    pass


def adding_contact():
    pass


def display_opt():
    try:
        options = ["Add", "Search", "Sort", "Edit", "Delete", "Display"]
        print("\n__Options__:")

        for key, option in enumerate(options, start=1):
            print(f"[{key}]. {option}]")

        opt = int(input("\nEnter your option [1-6]: "))

        if 1 > opt > 6:
            raise ValueError("Illegal input")
        else:
            return options[opt-1]

    except ValueError as error:
        print(f"Error 404 - Not Found: {error}")


def main():
    print("__Contact Book__")

    while True:
        opt = display_opt()


if __name__ == '__main__':
    main()