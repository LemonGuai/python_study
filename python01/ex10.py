# 创建使用类
class Player():
    def __init__(self,name):
        self.name = name
    
    def sayHello(self):
        print("hello ",self.name.title())
    
    def intro(self):
        print("i'm a player.")
    
curry = Player("curry")
print(curry.name)
curry.sayHello()
curry.intro()