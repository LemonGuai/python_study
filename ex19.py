# 定义一个函数,传入两个参数,第一个参数表示cheese的数量,第二个参数表示crackers的数量.输出cheeses和crackers的数量
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print(f"you have {cheese_count} cheeses!")
    print(f"you have {boxes_of_crackers} boxes of crackers!")
    print("man that's enough for a party.")
    print("get a blanket.\n")

# 直接传入两个参数
print("we can just give the function numbers directly:")
cheese_and_crackers(20, 30)

# 声明两个变量,并传入函数
print("or,we can use variables from our script:")
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# 在函数中对传入的参数进行加减处理
print("we can even do match inside too:")
cheese_and_crackers(10+20, 5+6)

 #使用函数cheese_and_crackers,在变量amount_of_cheese的基础上+100,amount_of_crakcers+1000,并作为参数传入函数
print("and we can combine the two, variables and match:")
cheese_and_crackers(amount_of_cheese+100, amount_of_crackers+1000)  