# 华氏温度转换成摄氏温度
def F_temp_change(temp):
    C = 5/9*(int(temp)-32)
    return round(C,2)

for i in range(0,300,20):
    C = F_temp_change(i)
    print(i, C)
    
