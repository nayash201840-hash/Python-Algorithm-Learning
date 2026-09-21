
def gcd_learning(a, b):

    if a < b:
        a, b = b, a

    print("Finding gcd(", a, ",", b, ")")

    step = 1

    while b != 0:

        quotient = a // b
        remainder = a % b

        print("Step", step, ":", a, "=", b, "*", quotient, "+", remainder)

        print("In Python, the remainder is calculated using the modulus operator '%'.")

        print("Here the remainder is:", remainder)

        input("Press Enter for the next step...")

        a = b
        b = remainder

        step += 1

    print("Final result: gcd =", a)

    return a
