from Learn.gcd_learning_mod import gcd_learning
from Learn.Prime_number_learning import check_prime
from Learn.Fibonic_series_learning import fibonacci_series
from Learn.Prime_factor_learning import prime_factors
from Learn.Array_revesel import array_reverse
from Learn.Array_count import count_occurrences
from Learn.Kth_smallest import kth_smallest
from Learn.converter_learning import converter


# Taking number input
def get_number(message):
    while True:
        number = input(message)

        if number == "":
            print("Please enter something.")
            continue

        number = int(number)

        return number


# Taking array input
def get_array():
    while True:
        values = input("Enter numbers separated by spaces: ")

        if values == "":
            print("Please enter some numbers.")
            continue

        numbers = converter(values)

        return numbers


def press_enter():
    input("\nPress Enter to continue...")


# Main menu
def main_menu():
    print("\n==========================================")
    print("       PYTHON ALGORITHM LEARNING")
    print("==========================================")

    print("\n1. GCD")
    print("2. Prime Number")
    print("3. Fibonacci Series")
    print("4. Prime Factorization")
    print("5. Array Reversal")
    print("6. Array Occurrence Counting")
    print("7. Kth Smallest Element")
    print("8. Exit")


# GCD
def run_gcd():
    print("\n================================")
    print("             GCD")
    print("================================")

    first_number = get_number("Enter first number: ")
    second_number = get_number("Enter second number: ")

    print("\nStarting GCD algorithm...")
    press_enter()

    result = gcd_learning(first_number, second_number)

    print("\nResult:")
    print("GCD =", result)


# Prime number
def run_prime():
    print("\n================================")
    print("         PRIME NUMBER")
    print("================================")

    number = get_number("Enter a number: ")

    print("\nStarting prime number algorithm...")
    press_enter()

    result = check_prime(number)

    print("\nResult:")

    if result:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")


# Fibonacci series
def run_fibonacci():
    print("\n================================")
    print("       FIBONACCI SERIES")
    print("================================")

    terms = get_number("Enter number of terms: ")

    if terms <= 0:
        print("Number of terms should be greater than 0.")
        return

    print("\nStarting Fibonacci algorithm...")
    press_enter()

    fibonacci_series(terms)


# Prime factors
def run_prime_factors():
    print("\n================================")
    print("       PRIME FACTORIZATION")
    print("================================")

    number = get_number("Enter a number: ")

    if number <= 0:
        print("Please enter a positive number.")
        return

    print("\nStarting prime factorization...")
    press_enter()

    Factors = prime_factors(number)

    print("\nPrime Factors:", Factors)


# Array reversal
def run_array_reverse():
    print("\n================================")
    print("          ARRAY REVERSAL")
    print("================================")

    numbers = get_array()

    print("\nOriginal array:", numbers)

    print("\nStarting array reversal...")
    press_enter()

    result = array_reverse(numbers)

    print("\nReversed array:", result)


# Array occurrence count
def run_array_count():
    print("\n================================")
    print("      ARRAY OCCURRENCE COUNT")
    print("================================")

    numbers = get_array()

    print("\nArray:", numbers)

    element = get_number("Enter element to count: ")

    print("\nStarting counting...")
    press_enter()

    result = count_occurrences(numbers, element)

    print("\nResult:")
    print(element, "occurs", result, "time(s).")


# Kth smallest element
def run_kth_smallest():
    print("\n================================")
    print("       KTH SMALLEST ELEMENT")
    print("================================")

    numbers = get_array()

    print("\nArray:", numbers)

    while True:
        k = get_number("Enter the value of K: ")

        if 1 <= k <= len(numbers):
            break

        print("K should be between 1 and", len(numbers))

    print("\nStarting Kth smallest algorithm...")
    press_enter()

    result = kth_smallest(numbers, k)

    print("\nResult:")
    print("Kth smallest element =", result)


# After a lesson
def lesson_finished():
    while True:
        print("\n================================")
        print("       LESSON COMPLETED")
        print("================================")

        print("\n1. Repeat lesson")
        print("2. Main menu")
        print("3. Exit")

        choice = input("\nEnter choice: ")

        if choice == "1":
            return "repeat"

        if choice == "2":
            return "menu"

        if choice == "3":
            return "exit"

        print("Please enter 1, 2 or 3.")


# Controls repeat, menu and exit
def run_lesson(lesson):
    while True:
        lesson()

        result = lesson_finished()

        if result == "repeat":
            continue

        if result == "menu":
            return True

        if result == "exit":
            return False


# Main program
program_running = True

while program_running:
    main_menu()

    choice = input("\nEnter your choice: ")

    if choice == "1":
        program_running = run_lesson(run_gcd)

    elif choice == "2":
        program_running = run_lesson(run_prime)

    elif choice == "3":
        program_running = run_lesson(run_fibonacci)

    elif choice == "4":
        program_running = run_lesson(run_prime_factors)

    elif choice == "5":
        program_running = run_lesson(run_array_reverse)

    elif choice == "6":
        program_running = run_lesson(run_array_count)

    elif choice == "7":
        program_running = run_lesson(run_kth_smallest)

    elif choice == "8":
        print("\nThank you for learning.")
        print("Keep practicing!")

        program_running = False

    else:
        print("\nPlease enter a choice from 1 to 8.")


print("\nProgram ended.")