def array_reverse(numbers):

    first = 0
    last = len(numbers) - 1

    while first < last:

        print(f"""
        First index: {first}
        Last index: {last}

        Before swapping: {numbers}

        Swapping {numbers[first]} and {numbers[last]}
        """)



        temp = numbers[first]
        numbers[first] = numbers[last]
        numbers[last] = temp

        print("After swapping:", numbers)

        first = first + 1
        last = last - 1

        print("Moving first index to:", first)
        print("Moving last index to:", last)

        input("\nPress Enter to continue...")

    return numbers
