def count_occurrences(numbers, search_element):

    count = 0

    print("\nStarting search...")
    print("Element to search:", search_element)
    print("Starting count:", count)

    for i in range(len(numbers)):

        print("\n-----------------------------")
        print("Index:", i)
        print("Element at this index:", numbers[i])
        print("Searching for:", search_element)

        if numbers[i] == search_element:

            count = count + 1

            print("Element matched!")
            print("Count increased to:", count)

        else:

            print("Element did not match.")
            print("Count remains:", count)

        print("Array:", numbers)

        input("\nPress Enter to continue...")

    print("\n-----------------------------")
    print("Search completed.")
    print("Element:", search_element)
    print("Number of occurrences:", count)

    return count