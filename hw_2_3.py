# 角谷猜想
a = input('请输入一个整数')
int_a = int(a)

while int_a != 1:
    if int_a % 2 == 0:
        print(f"{int_a}/2 = {int_a / 2}")
        int_a = int_a / 2
    else:
        print(f"{int_a}*3 + 1 = {int_a * 3 + 1}")
        int_a = int_a * 3 + 1
print(f'结果成立,最终a为:{int_a}')
