n = int(input("请输入一个整数:"))
mylist = []
count = 0
for i in range(1, 100):
    if i % n != 0 and i // 10 != n and i % 10 != n:
        print(f"{i},", end='')
        count += 1
    if count == 10:
        print('\r')
        count = 0

