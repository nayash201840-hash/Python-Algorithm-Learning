def prime_factors(n):

    Factors = []

    i = 2

    print("\nStarting Prime Factorization")
    print("Number entered:", n)

    while n != 1:

        print("\n-----------------------------")
        print("Number being checked:", n)
        print("Factor being taken:", i)

        if n % i == 0:

            print("The number is divisible by", i)

            result = n // i

            print("Division:", n, "/", i)
            print("Result:", result)

            Factors.append(i)

            print("Factor stored:", i)
            print("Factors so far:", Factors)

            n = result

            print("Remaining number:", n)

        else:

            print(i, "is not divisible by", n)

            i = i + 1

            print("Checking next factor:", i)

        input("\nPress Enter to continue...")


    print("\n=============================")
    print("Prime Factors:", Factors)
    print("=============================")
