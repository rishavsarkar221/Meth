def median():
    nums = []

    times = input("How many numbers u want to enter? ")

    for i in range(1, int(times) + 1):
        n = input(f"Enter Number {i}: ")
        nums.append(int(n))

    if len(nums) % 2 != 0:
        print(nums[
            round((len(nums)/2))
        ])

    elif len(nums) % 2 == 0:
        print(
            nums[round((len(nums) / 2) - 1)], 
            'and',
            nums[round(len(nums) / 2)]
        )


def union_sets():
    sets1 = [1, 2, 3, 4, 8]
    sets2 = [2, 4, 7, 8]

    repeated = []

    for i in sets1:
        if i in sets2:
            repeated.append(i)

    if len(repeated) != 0: print(repeated)
    else: print("NO repeating")


def U_sets():
    word1 = input("Enter First Word: ")
    word2 = input("Enter Second Word: ")

    arr1 = []
    arr2 = []

    sets = []

    for j in word1:
        if j.upper() not in arr1: arr1.append(j.upper())

    for i in word2:
        if i.upper() not in arr2: arr2.append(i.upper())

    for k in arr1:
        sets.append(k)
    
    for h in arr2:
        if h not in sets: sets.append(h)

    print(sets)


a = input("What do u want to output?\nMedian, union sets, u sets: ")
if a.lower() == 'median': median()
elif a.lower() == 'union sets': union_sets()
elif a.lower() == 'u sets': U_sets()
else: print("Enter something valid noob")