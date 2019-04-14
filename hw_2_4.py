# 阶乘和
str_n = input("请输入整数n:")
n = int(str_n)
sum = 1

for i in range(1,n+1):
    # if i == 1:
    #     print(i)
    #     i += 1
    # else:
        sum = sum + i*(i-1)       
        i += 1


print(sum)
