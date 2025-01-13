def prime_range():
    prime_number = []
    start, end = get_points()

    for number in range(start,end+1):
        if number <= 1:
            continue

        num_prime = True

        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                num_prime = False
                break

        if num_prime:
            prime_number.append(number)
                
    return prime_number


def get_points():
    try:
        starting_point = int(input("Start point: "))
        ending_point = int(input("End point: "))
        return starting_point,ending_point
    
    except TypeError:
        print("Invalid Entry")


def get_options():
    opt = {
        1 : "Prime Range",
        2 : "Check Primality",
        3 : "Listing First N Primes"
    }

    try:
        print("__Option__")
        for key, value in opt.items():
            print(f"{key}: {value}")

        opt = int(input("\nSelect Option: "))
        print()

        return opt

    except TypeError:
        print("Invalid Entry")


def prime_check():
    try:
        number = int(input("Enter a number: "))
        if number <= 1:
            return False

        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                return False
        return True

    except (ValueError, TypeError):
        print("Invalid Entry")


def prime_n_term():
    try:
        prime_list = []
        number = int(input("Enter a number: "))

        for num in range(1,number+1):
            if num <= 1:
                continue

            num_is_prime = True

            for i in range(2,int(num**0.5)+1):
                if num % i == 0:
                    num_is_prime = False
                    break

            if num_is_prime:
                prime_list.append(number)

        return prime_list



    except (ValueError, TypeError):
        print("Invalid Entry")


def main():
    selected_opt = get_options()

    match selected_opt:
        case 1:
            prime_numbers = prime_range()
            print(prime_numbers)
        case 2:
            check_prime = prime_check()
            print(check_prime)
        case 3:
            n_term = prime_n_term()
            print(n_term)
    


if __name__ == '__main__':
    main()