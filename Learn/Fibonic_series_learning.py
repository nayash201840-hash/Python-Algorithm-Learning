# Fibonacci Series

def fibonacci_series(terms):

    a = 0
    b = 1

    for i in range(terms):

        print("\nTerm:", i + 1)

        if i == 0:
            print("Number:", a)
            input("\nPress Enter to continue...")

        elif i == 1:
            print("Number:", b)

        else:
            c = a + b

            print("Previous two numbers:", a, "+", b)
            print("New number:", c)

            a = b
            b = c


