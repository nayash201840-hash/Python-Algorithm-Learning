```python
from Learn.gcd_learning_mod import gcd_learning
from Learn.Prime_number_learning import check_prime
from Learn.Fibonic_series_learning import fibonacci_series
from Learn.Prime_factor_learning import prime_factors
from Learn.Array_revesel import array_reverse
from Learn.Array_count import count_occurrences
from Learn.Kth_smallest import kth_smallest
from Learn.converter_learning import converter


def list_of_values():
    while True:
        values = input("Enter numbers separated by spaces: ")

        if values == "":
            print("Please enter some numbers.")
            continue

        numbers = converter(values)

        return numbers


def option_input(message):
    while True:
        number = input(message)

        if number == "":
            print("Please enter something.")
            continue

        if number.isdigit():
            return int(number)

        print("Please enter a number.")


def press_enter():
    input("\nPress Enter to continue...")


def lesson_finished():

    while True:

        print("""
            1. Repeat lesson
            2. Main menu
            3. Exit
        """)

        option = input("\nEnter a number: ")

        if option == "1":
            return "repeat"

        elif option == "2":
            return "menu"

        elif option == "3":
            return "exit"

        else:
            print("\nSelect from given option")


def start_lesson(lesson):

    while True:
        lesson()

        To_do = lesson_finished()

        if To_do == "repeat":
            continue

        elif To_do == "menu":
            return True

        elif To_do == "exit":
            return False


def main_menu():

    programming = True

    while programming:

        print("""
        ==========================================
              PYTHON ALGORITHM LEARNING
        ==========================================

        1. GCD
        2. Prime Number
        3. Fibonacci Series
        4. Prime Factorization
        5. Array Reversal
        6. Array Occurrence Counting
        7. Kth Smallest Element
        8. Exit
        """)

        option = option_input("Enter your requirement: ")

        if option == 1:
            programming = start_lesson(gcd)

        elif option == 2:
            programming = start_lesson(prime_num)

        elif option == 3:
            programming = start_lesson(fibonacci)

        elif option == 4:
            programming = start_lesson(prime_factor)

        elif option == 5:
            programming = start_lesson(reversal)

        elif option == 6:
            programming = start_lesson(counting)

        elif option == 7:
            programming = start_lesson(kth)

        elif option == 8:
            print("""
            Thank you for joining us.

            Keep Learning and Enjoying
            """)
            programming = False

        else:
            print("\nPlease enter a number from 1 to 8.")


def gcd():

    print("             GCD")

    fst = option_input("Enter first number: ")
    sec = option_input("Enter second number: ")

    print("\nStarting GCD algorithm...")
    press_enter()

    result = gcd_learning(fst, sec)

    print("\nResult:")
    print("GCD =", result)


def prime_num():

    print("         PRIME NUMBER")

    number = option_input("Enter a number: ")

    print("\nStarting prime number algorithm...")
    press_enter()

    result = check_prime(number)

    print("\nResult:")

    if result:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


def fibonacci():

    print("       FIBONACCI SERIES")

    terms = option_input("Enter number of terms: ")

    if terms <= 0:
        print("Number of terms should be greater than 0.")
        return

    print("\nStarting Fibonacci algorithm...")
    press_enter()

    fibonacci_series(terms)


def prime_factor():

    print("       PRIME FACTORIZATION")

    number = option_input("Enter a number: ")

    if number <= 0:
        print("Please enter a positive number.")
        return

    print("\nStarting prime factorization...")
    press_enter()

    Factors = prime_factors(number)

    print("\nPrime Factors:", Factors)


def reversal():

    print("          ARRAY REVERSAL")

    numbers = list_of_values()

    print("\nOriginal array:", numbers)

    print("\nStarting array reversal...")
    press_enter()

    result = array_reverse(numbers)

    print("\nReversed array:", result)


def counting():

    print("      ARRAY OCCURRENCE COUNT")

    numbers = list_of_values()

    print("\nArray:", numbers)

    element = option_input("Enter element to count: ")

    print("\nStarting counting...")
    press_enter()

    result = count_occurrences(numbers, element)

    print("\nResult:")
    print(element, "occurs", result, "time(s).")


def kth():

    print("       KTH SMALLEST ELEMENT")

    numbers = list_of_values()

    print("\nArray:", numbers)

    while True:

        k = option_input("Enter the value of K: ")

        if 1 <= k <= len(numbers):
            break

        print("K should be between 1 and", len(numbers))

    print("\nStarting Kth smallest algorithm...")
    press_enter()

    result = kth_smallest(numbers, k)

    print("\nResult:")
    print("Kth smallest element =", result)
```
