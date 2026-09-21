# Prime Number Learning Program

import math


def check_prime(number):

    print("Checking number:", number)

    if number <= 1:
        print(number, "is NOT a prime number")
        return

    square_root = int(math.sqrt(number))

    print("Square root of", number, "is", square_root)

    for i in range(2, square_root + 1):

        print("Checking:", number, "%", i)

        if number % i == 0:

            print(number, "is divisible by", i)
            print(number, "is NOT a prime number")

            input("Press Enter to exit...")
            return

        print(number, "is NOT divisible by", i)

        input("Press Enter to check the next number...")

    print(number, "was not divisible by any number")
    print(number, "is a PRIME number")
