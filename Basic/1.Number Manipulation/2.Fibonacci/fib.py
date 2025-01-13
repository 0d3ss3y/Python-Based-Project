def option():
    options = {
        1 : "Generate Fibonacci sequence up to N term",
        2 : "Find Nth Fibonacci number"
    }

    print("__Options__")

    for key, value in options.items():
        print(f"{key}: {value}")

    opt = int(input("Enter a option key [1-2]\n> "))

    if opt > 2 or opt < 1:
        print("Invalid option")
        option()
    else:
        return opt


def get_fib(n):
    seq = generate_fibonacci(n)
    return seq[n-1]


def get_input():
    try:
        number = int(input("Enter a number: "))
        return number
    except (ValueError, TypeError):
        print("Invalid input")


def generate_fibonacci(n):
    if n == 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0,1]

    seq = [0, 1]
    for i in range(2, n):
        seq.append(seq[-1] + seq[-2])
    return seq


def main():
    opt = option()
    num = get_input()

    match opt:
        case (1):
            seq = generate_fibonacci(num)
            print(seq)
        case (2):
            fib_num = get_fib(num)
            print(fib_num)


if __name__ == '__main__':
    main()