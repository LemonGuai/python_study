# mylist = [["a1"], ["b1", "b2"], ["c1", "c2", "c3"], ["d1", "d2", "d3", "d4"]]
# # mylist_stored = mylist
# result = []
# for i in mylist:
#     item = i.pop()
#     result.append(item)

# print(mylist)
# print(result)
# class work1:
#     def __option1(self):
#         .......
#     def __option2(self):
#         .......
#     def __option3(self):
#         .......

#     def handle(self, arg1):
#         self.__option1()
#         self.__option2()
#         self.__option3()

# a = work1()
# arg1 = input("请输入参数值:")
# a.handle(arg1)

# class Test:
#     def __init(self):
#         pass

#     def f(self):
#         print('Hello, World!')

# if __name__ == '__main__':
#     Test().f()

# import datetime
# from datetime import date

# a = date.today()
# # print(a）
# a, b = eval(input())
# print(a/b)
# a = 5
# if not 1<= a <= 4:
#     print("true")
# files = ['这是第{}行'.format(i) for i in range(10)]
# print(files)
# print
# a = [1,2,3]
# print(a)

# filename='./python_study/ex16.txt'
# with open(filename, 'r') as data:
#     text = data.read()
#     print(text)


def add(a, b):
    return a + b


def test1():
    assert 2 == add(1, 1)


def test2():
    assert 1 != add(1, 1)
