# import math
def prime_num(n):
    if n == 1:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
    return True


def num_judge(n):
    num_1 = 1
    while num_1 <= n:
        num_2 = n - num_1
        if num_1 >= num_2:
            break
        if prime_num(num_1) and prime_num(num_2):
            return num_1, num_2
        num_1 += 1


number = int(input('请输入一个正整数'))
if number % 2 == 0 and number >= 4:
    a, b = num_judge(number)
    print(f"{number},{a},{b}")
