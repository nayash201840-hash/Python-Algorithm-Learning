def count_occurrences(numbers, search_element):

    count = 0
    num=numbers
    find=search_element


    print("""
    Element to search: {find}""")

    for i in range(len(numbers)):

       
        print("""
        Index: {i}
        Element at this index: {numbers[i]}
        Searching for: {find}
        """)
        

        if numbers[i] == find:

            count = count + 1

            print("Element matched!")
            print("Count increased to:", count)

        else:

            print("Element did not match.")
            print("Count remains:", count)

        print("Array:", numbers)

        input("\nPress Enter to continue...")

    
    print('''
    Search completed

    Element: {find}
    Number of times: {count}''')

    return count
