def ex33_1(number, len_range):
    i = 0
    numbers = []

    while i < number:
        print(f"at the top i is {i}.")
        numbers.append(i)

        i += len_range
        print("numbers now:", numbers)
        print(f"at the bottom i is {i}.")

    print("the numbers:")

    for num in numbers:
        print(num)


ex33_1(8, 2)