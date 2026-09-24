
def gcd_learning(a, b):

    if a < b:
        a, b = b, a

    print(f"""
        Finding gcd {a} , {b} 
        FACT: In Python, the remainder is calculated using the modulus operator '%'.
    """)

    step=1
    
    while b != 0:

        quotient = a // b
        remainder = a % b

        print("Step", step, ":", a, "=", b, "*", quotient, "+", remainder)



        print("Here the remainder is:", remainder)

        input("Press Enter for the next step...")

        a = b
        b = remainder

        step += 1

    print("Final result: gcd =", a)

    return a
