
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
            input("\nPress Enter to continue...")

        else:
            c = a + b

            print(f"""
            Previous two numbers: {a} + {b})
            New number: {c}
            """)
            input("\nPress Enter to continue...")

            a = b
            b = c


