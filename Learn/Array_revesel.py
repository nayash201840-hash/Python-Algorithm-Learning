def array_reverse(num):

    f = 0
    l = len(num) - 1

    while f < l :

        print(f"""
        First index: {f}
        Last index: {l}

        Before swapping: {num}

        Swapping {num[f]} and {num[l]}
        """)



        temp = num[f]
        num[f] = num[l]
        num[l] = temp

        print("After swapping:", num)

        f = f + 1
        l = l - 1

        print("Moving first index to:", f)
        print("Moving last index to:", l)

        input("\nPress Enter to continue...")

    return num
