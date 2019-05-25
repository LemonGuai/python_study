# # this goes in mystuff.py
# def apple():
#     print('i am apples!')


# # this is just a variable
# tangerine = "living reflection of a dream"
class MyStuff(object):
    def __init__(self):
        self.tangerine = "and now a thousand years between"

    def apple(self):
        print("i am classy apples!")


thing = MyStuff()
thing.apple()
print(thing.tangerine)