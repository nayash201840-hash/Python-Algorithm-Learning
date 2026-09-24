def check_prime(number):

    print("Checking number:", number)

    if number <= 1:


        print(number, "is NOT a prime number")

        return False


    square_root = int(number ** 0.5)


    print(f"""
    Square root of  {number} is {square_root}
    FACT: Check the divisibility till the integer value of square root for the Prime Number.
    """)



    for i in range(2, square_root + 1):

        print("Checking:", number, "%", i)

        if number % i == 0:

            print(f"""
            {number} is divisible by {i}
            {number} is NOT a prime number.
            """)

            input("Press Enter to exit...")
            return

        print(number, "is NOT divisible by", i)

        input("Press Enter to check the next number...")

        

    print(f"""
    {number} is not divisible by {i}
    {number} is  a PRIME number.
    """)
    
