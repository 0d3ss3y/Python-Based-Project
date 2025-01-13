from random import randint


def play(actual_number):
    strike = 3

    while strike != 0:
        guess_number = int(input("Guess a number between 0 and 20: "))

        if guess_number == actual_number:
            print(f"Correct! You guessed the correct number! with {strike} attempts left")
            break
        elif guess_number < actual_number:
            strike -= 1
            print(f"Your guess is lower than actual number")
        else:
            strike -= 1
            print(f"Your guess is higher than actual number")
    else:
        print(f"Sorry, you lost to guess the correct number!\n correct number is {actual_number}")


def main():
    gen_num = randint(0, 20)

    print("Welcome to Mastermind!")
    play(gen_num)


if __name__ == '__main__':
    main()