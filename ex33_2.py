i = 0
numbers = []

for i in range(0, 6):
    print(f"at the top i is {i}.")
    numbers.append(i)
    print("numbers now:", numbers)
    print(f"at the bottom i is {i}.")

print("the numbers:")

for num in numbers:
    print(num)