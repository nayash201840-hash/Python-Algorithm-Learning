def kth_smallest(numbers, k):

    print("\nOriginal list:", numbers)
    print("K value:", k)

    print("\nSorting the list...")

    numbers.sort()

    print("Sorted list:", numbers)

    position = k - 1

    print("\nKth position:", k)
    print("Python index:", position)

    kth_value = numbers[position]

    print("Kth smallest value:", kth_value)

    return kth_value


