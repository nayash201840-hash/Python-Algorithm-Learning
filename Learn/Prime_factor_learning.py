def prime_factors(n):

    Factors = []

    i = 2

    print(f"""\nStarting Prime Factorization")
    print("Number entered:", n""")

    while n != 1:

        print(f"""
        -----------------------------
        Number being checked: {n}
        Factor being taken: {i}
        -----------------------------
        """)

        if n % i == 0:

            print("The number is divisible by", i)

            result = n // i

            print(f"""  
            --->Division: {n} / {i}

            ---> Result: {result}
            """)

            Factors.append(i)

            print(f"""
            --->Factor stored: {i}
            --->Factors so far: {Factors}
            """)

            n = result

            print("Remaining number:", n)

        else:

            print(i, "is not divisible by", n)

            i = i + 1

            print("Checking next factor:", i)

        input("\nPress Enter to continue...")


    print(f"""
    x-x-x-x-x-x-x-x-x-x-x-x-x-x-x")
    Prime Factors: {Factors}
    print("-x-x-x-x-x-x-x-x-x-x-x-x-x-x-x""")
