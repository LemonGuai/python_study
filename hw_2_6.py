for i in range(3,30):
    num = i * 37
    if num < 1000:
        a = num % 10
        b = (num % 100)//10
        c = num // 100
        sum_1 = b*100+a*10+c
        sum_2 = a*100+c*10+b
    if sum_1 % 37 == 0 and sum_2 % 37 == 0:
        print("命题为真")